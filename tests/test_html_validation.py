import pytest
from bs4 import BeautifulSoup
import os

def test_html_validity():
    """Vérifie la validité basique du HTML"""
    for filename in os.listdir('dist'):
        if filename.endswith('.html'):
            with open(os.path.join('dist', filename), 'r', encoding='utf-8') as f:
                soup = BeautifulSoup(f, 'html.parser')
                
                # Vérifie la structure de base
                assert soup.find('html').get('lang'), "HTML should have lang attribute"
                assert soup.find('head'), "HTML should have head section"
                assert soup.find('body'), "HTML should have body section"
                assert soup.find('meta', {'charset': True}), "HTML should have charset meta tag" 