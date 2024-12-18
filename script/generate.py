import sys
import os
import markdown
import csv
from jinja2 import Environment, FileSystemLoader
import re

def extract_metadata(md_content):
    md = markdown.Markdown(extensions=['meta'])
    html_content = md.convert(md_content)
    metadata = md.Meta if hasattr(md, 'Meta') else {}
    
    for key, value in metadata.items():
        metadata[key] = value[0] if isinstance(value, list) else value
    
    if 'title' not in metadata:
        match = re.search(r'^#\s+(.+)$', md_content, re.MULTILINE)
        metadata['title'] = match.group(1) if match else 'Sans titre'
    
    if 'description' not in metadata:
        match = re.search(r'\n\n(.+?)\n\n', md_content, re.DOTALL)
        metadata['description'] = match.group(1) if match else 'Pas de description disponible.'
    
    return html_content, metadata

def get_image_path(filename):
    match = re.search(r'\d{4}-\d{2}-\d{2}-(.+)\.md$', filename)
    event_id = match.group(1) if match else 'event'
    image_path = f'../ressource/{event_id}.webp'
    
    return image_path if os.path.exists(f'ressource/{event_id}.webp') else '../ressource/placeholder.webp'

def process_markdown(input_file, output_file, template):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    html_content, metadata = extract_metadata(content)
    image_path = get_image_path(os.path.basename(input_file))
    
    rendered = template.render(
        content=html_content,
        image_path=image_path,
        base_path="..",
        **metadata
    )
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(rendered)
    
    return metadata, image_path

def process_csv(input_file, output_file, template):
    with open(input_file, 'r', encoding='utf-8') as f:
        members = list(csv.DictReader(f))
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(template.render(members=members, base_path=".."))

def main(input_folder):
    if os.path.exists('dist'):
        for file in os.listdir('dist'):
            os.remove(os.path.join('dist', file))
    
    env = Environment(loader=FileSystemLoader('src'))
    templates = {
        'article': env.get_template('detail.html'),
        'members': env.get_template('membres.html'),
        'index': env.get_template('index.html')
    }
    
    os.makedirs('dist', exist_ok=True)
    articles = []
    
    with open(os.path.join('dist', 'membres.html'), 'w', encoding='utf-8') as f:
        f.write(templates['members'].render(base_path=".."))
    
    for filename in os.listdir(input_folder):
        input_file = os.path.join(input_folder, filename)
        output_file = os.path.join('dist', os.path.splitext(filename)[0] + '.html')
        
        if filename.endswith('.md'):
            metadata, image_path = process_markdown(input_file, output_file, templates['article'])
            articles.append({
                'filename': os.path.splitext(filename)[0] + '.html',
                'title': metadata['title'],
                'date': metadata.get('date', 'Date non spécifiée'),
                'description': metadata.get('description', ''),
                'image_path': image_path
            })
            print(f"✅ Processed: {filename}")
        elif filename.endswith('.csv'):
            process_csv(input_file, output_file, templates['members'])
    
    with open(os.path.join('dist', 'index.html'), 'w', encoding='utf-8') as f:
        f.write(templates['index'].render(articles=articles, base_path="."))
    
    print(f"\n✅ Generated {len(articles)} articles")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("❌ Usage: python generate.py <input_folder>")
        sys.exit(1)
    
    input_folder = sys.argv[1]
    if not os.path.exists(input_folder):
        print(f"❌ Input folder '{input_folder}' does not exist")
        sys.exit(1)
    
    main(input_folder)
