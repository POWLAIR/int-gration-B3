import os
import markdown
import re

def test_markdown_metadata():
    """Vérifie que les fichiers Markdown contiennent les métadonnées requises"""
    content_dir = 'content'
    if os.path.exists(content_dir):
        for filename in os.listdir(content_dir):
            if filename.endswith('.md'):
                with open(os.path.join(content_dir, filename), 'r', encoding='utf-8') as f:
                    content = f.read()
                    md = markdown.Markdown(extensions=['meta'])
                    md.convert(content)
                    
                    # Vérifie les métadonnées essentielles
                    assert hasattr(md, 'Meta'), f"File {filename} should have metadata"
                    assert 'title' in md.Meta or re.search(r'^#\s+(.+)$', content, re.MULTILINE), \
                        f"File {filename} should have a title in metadata or as h1" 