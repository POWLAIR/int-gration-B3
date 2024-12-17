import pytest
import os
import shutil

@pytest.fixture(autouse=True)
def setup_test_environment():
    """Prépare l'environnement de test avant chaque test"""
    # Crée les dossiers nécessaires s'ils n'existent pas
    os.makedirs('dist', exist_ok=True)
    os.makedirs('content', exist_ok=True)
    os.makedirs('ressource', exist_ok=True)
    os.makedirs('styles', exist_ok=True)
    
    yield
    
    # Nettoyage après les tests si nécessaire
    # shutil.rmtree('dist')  # Décommentez si vous voulez nettoyer après les tests 