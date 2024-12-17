from bs4 import BeautifulSoup
import os

def test_internal_links():
    with open('dist/index.html', 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
        
    # Vérifie tous les liens
    for link in soup.find_all('a'):
        href = link.get('href')
        if href and not href.startswith(('http://', 'https://', '#')):
            # Convertit le chemin relatif en chemin absolu
            if href.startswith('../'):
                href = href[3:]
            # Vérifie dans le dossier dist/
            full_path = os.path.join('dist', os.path.basename(href))
            assert os.path.exists(full_path), f"Link target {href} does not exist"
