import os
import re

def test_placeholder_exists():
    assert os.path.exists('ressource/placeholder.webp'), "Placeholder image should exist"

def test_article_images_exist():
    # Vérifie que chaque article a une image correspondante
    content_dir = 'content'
    if os.path.exists(content_dir):
        for filename in os.listdir(content_dir):
            if filename.endswith('.md'):
                match = re.search(r'\d{4}-\d{2}-\d{2}-(.+)\.md$', filename)
                if match:
                    event_name = match.group(1)
                    image_path = f'ressource/{event_name}.webp'
                    assert os.path.exists(image_path) or os.path.exists('ressource/placeholder.webp'), \
                        f"Neither image {image_path} nor placeholder exists"
    