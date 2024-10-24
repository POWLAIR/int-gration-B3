import sys
import os
import markdown
import csv
from jinja2 import Environment, FileSystemLoader
import re

def convert_md_to_html(md_content):
    return markdown.markdown(md_content, extensions=['meta'])

def extract_first_h1(md_content):
    match = re.search(r'^#\s+(.+)$', md_content, re.MULTILINE)
    return match.group(1) if match else 'Sans titre'

def extract_first_paragraph(md_content):
    match = re.search(r'\n\n(.+?)\n\n', md_content, re.DOTALL)
    return match.group(1) if match else 'Pas de description disponible.'

def process_markdown_file(input_file, output_file, template):
    with open(input_file, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    md = markdown.Markdown(extensions=['meta'])
    html_content = md.convert(md_content)
    
    metadata = md.Meta
    for key, value in metadata.items():
        metadata[key] = value[0] if len(value) == 1 else value
    
    if 'title' not in metadata:
        metadata['title'] = extract_first_h1(md_content)
    else:
        metadata['title'] = metadata['title'][0]
    
    if 'description' not in metadata:
        metadata['description'] = extract_first_paragraph(md_content)
    
    # Extract the event identifier from the filename
    event_identifier = re.search(r'(\d{4}-\d{2}-\d{2}-(.+))\.md$', os.path.basename(input_file)).group(2)
    image_filename = f'{event_identifier}.webp'
    image_path = f'../ressource/{image_filename}'
    
    # Check if the image exists, otherwise use a placeholder
    if not os.path.exists(os.path.join('ressource', image_filename)):
        image_path = '../ressource/placeholder.webp'
    
    rendered_html = template.render(content=html_content, image_path=image_path, **metadata, base_path="../src/")
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(rendered_html)
    
    return metadata, image_path

def process_csv_file(input_file, output_file, template):
    members = []
    with open(input_file, 'r', encoding='utf-8') as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            members.append(row)
    
    rendered_html = template.render(members=members, base_path="../src/")
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(rendered_html)

def main(input_folder):
    env = Environment(loader=FileSystemLoader('src'))
    article_template = env.get_template('detail.html')
    members_template = env.get_template('membres.html')
    index_template = env.get_template('index.html')
    
    output_folder = 'dist'
    os.makedirs(output_folder, exist_ok=True)
    
    articles = []
    
    for filename in os.listdir(input_folder):
        input_file = os.path.join(input_folder, filename)
        output_filename = os.path.splitext(filename)[0] + '.html'
        output_path = os.path.join(output_folder, output_filename)
        
        if filename.endswith('.md'):
            metadata, image_path = process_markdown_file(input_file, output_path, article_template)
            
            articles.append({
                'filename': f'../dist/{output_filename}',
                'title': metadata['title'],
                'date': metadata.get('date', ''),
                'description': metadata.get('description', ''),
                'image_path': image_path
            })
            
            print(f"Processed Markdown file: {filename}")
        elif filename.endswith('.csv'):
            process_csv_file(input_file, output_path, members_template)
            print(f"Processed CSV file: {filename}")
    
    # Générer la page d'index dans src
    index_output = os.path.join('src', 'index.html')
    with open(index_output, 'w', encoding='utf-8') as f:
        f.write(index_template.render(articles=articles))
    print("Generated index page in src folder")
    print(f"Number of articles processed: {len(articles)}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python generate.py <input_folder>")
        sys.exit(1)
    
    input_folder = sys.argv[1]
    main(input_folder)
