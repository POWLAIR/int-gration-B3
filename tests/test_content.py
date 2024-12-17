import os
from bs4 import BeautifulSoup

def test_generated_files():
    # Vérifie que les fichiers essentiels existent
    assert os.path.exists('dist/index.html'), "Index.html should exist"
    assert os.path.exists('styles/main.css'), "CSS file should exist"
    
    # Vérifie que les fichiers ne sont pas vides
    assert os.path.getsize('dist/index.html') > 0, "Index.html should not be empty"
    assert os.path.getsize('styles/main.css') > 0, "CSS file should not be empty"

def test_article_content():
    with open('dist/index.html', 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
    
    articles = soup.find_all(class_='article-card')
    assert len(articles) > 0, "Should have at least one article"
    
    for article in articles:
        assert article.find('h3'), "Article should have a title"
        assert article.find('img'), "Article should have an image"
        assert article.find(class_='description'), "Article should have a description"
