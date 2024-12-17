import os
import re

def test_css_file():
    assert os.path.exists('styles/main.css'), "CSS file should exist"
    
    with open('styles/main.css', 'r', encoding='utf-8') as f:
        css_content = f.read()
    
    # Vérifie les règles CSS essentielles
    essential_selectors = [
        'body',
        'header',
        '.article-card',
        '.article-image',
        '.members-table'
    ]
    
    for selector in essential_selectors:
        assert re.search(rf'{selector}\s*{{', css_content), f"CSS should contain {selector} rules"
