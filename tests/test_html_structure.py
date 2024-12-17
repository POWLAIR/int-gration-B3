from bs4 import BeautifulSoup
import os

def read_html(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return BeautifulSoup(f, 'html.parser')

def test_index_structure():
    soup = read_html('dist/index.html')
    
    # Test des éléments essentiels
    assert soup.find('header'), "Header should exist"
    assert soup.find('main'), "Main content should exist"
    assert soup.find('footer'), "Footer should exist"
    
    # Test de la navigation
    nav = soup.find('nav')
    assert nav, "Navigation should exist"
    assert nav.find_all('a'), "Navigation should contain links"

def test_article_structure():
    for filename in os.listdir('dist'):
        if filename.endswith('.html') and filename != 'index.html' and filename != 'membres.html':
            soup = read_html(f'dist/{filename}')
            
            # Test des éléments d'article
            article = soup.find('article')
            assert article, f"Article element missing in {filename}"
            assert article.find('h2'), "Article should have a title"
            assert article.find('img'), "Article should have an image"

