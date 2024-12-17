# Vivre aux Lilas

## Introduction

Ce projet génère un site web statique à partir de fichiers Markdown et CSV. Il utilise Python pour le traitement des fichiers et Jinja2 pour le templating. Les pages générées incluent des articles avec des images associées et une page de membres.

## Prérequis Systèmes

- **Système d'exploitation** : Windows 10 ou supérieur
- **Python** : Version 3.12 ou supérieure
- **Pip** : Gestionnaire de paquets Python
- **Modules Python** : `markdown`, `jinja2`

## Installation sur Windows

1. **Installer Python et Pip** :

   - Téléchargez et installez Python depuis le site officiel : [python.org](https://www.python.org/downloads/)
   - Assurez-vous de cocher l'option "Add Python to PATH" lors de l'installation.

2. **Installer les modules Python requis** :
   Ouvrez l'invite de commande (CMD) et exécutez :
   ```bash
   pip install markdown jinja2
   ```

## Commandes de Build

Pour générer le site, utilisez le script `generate.py` :

1. **Exécuter le script de génération** :
   Ouvrez l'invite de commande dans le répertoire du projet et exécutez :

   ```bash
   python script/generate.py chemin\vers\dossier_entree
   ```

   - `chemin\vers\dossier_entree` : Le chemin vers le dossier contenant les fichiers Markdown et CSV.

## Options et Commandes

- **Aucun argument supplémentaire** : Le script prend un seul argument, le chemin vers le dossier d'entrée.
- **Structure des fichiers** : Assurez-vous que les fichiers Markdown suivent le format `YYYY-MM-DD-nom-evenement.md` et que les images correspondantes sont nommées `nom-evenement.webp` dans le dossier `ressource`.

## Membres du Groupe

- Claverie Paul.
- Roupert Bastien.

## Notes

- Les images doivent être placées dans le dossier `ressource` et doivent correspondre aux événements décrits dans les fichiers Markdown.
- Un placeholder est utilisé si aucune image spécifique n'est trouvée pour un article.
- Le site généré est statique et ne nécessite pas de serveur pour être consulté.

## Explication du Code

### Structure du Projet

- **script/generate.py** : Le script principal qui génère le site. Il lit les fichiers Markdown et CSV, extrait les métadonnées, et utilise Jinja2 pour générer les fichiers HTML.

  - **Fonctions principales** :
    - `convert_md_to_html`: Convertit le contenu Markdown en HTML.
    - `extract_first_h1`: Extrait le premier titre h1 du fichier Markdown pour l'utiliser comme titre de l'article.
    - `process_markdown_file`: Traite chaque fichier Markdown, extrait les métadonnées, et génère le fichier HTML correspondant.
    - `process_csv_file`: Traite les fichiers CSV pour générer la page des membres.
    - `main`: Fonction principale qui orchestre le traitement des fichiers et la génération des pages.

- **src/** : Contient les templates HTML utilisés par Jinja2 pour générer les pages.

  - **index.html** : Template pour la page d'accueil qui liste tous les articles.
  - **detail.html** : Template pour la page de détail de chaque article.
  - **membres.html** : Template pour la page des membres.

- **styles/main.css** : Fichier CSS contenant les styles pour le site. Il définit les styles globaux, ainsi que des styles spécifiques pour les articles et les membres.

### Fonctionnalités Clés

- **Génération Automatique** : Le script génère automatiquement les pages HTML à partir des fichiers Markdown et CSV.
- **Gestion des Images** : Associe automatiquement les images aux articles en fonction du nom de fichier. Utilise un placeholder si l'image n'est pas disponible.
- **Design Responsive** : Le site utilise des styles CSS pour s'adapter à différentes tailles d'écran.

## CI/CD

Ce projet utilise GitHub Actions pour l'intégration et le déploiement continus.

### Déploiement automatique

Le site est automatiquement déployé sur GitHub Pages à chaque push sur la branche `main`.
Vous pouvez accéder au site à l'adresse : https://<username>.github.io/<repository>/

### Workflow

Le workflow CI/CD :

1. Configure l'environnement Python
2. Installe les dépendances nécessaires
3. Génère les fichiers statiques
4. Déploie le site sur GitHub Pages

Pour plus de détails, consultez le fichier `.github/workflows/main.yml`.

## Tests

Pour exécuter les tests :

1. Installez les dépendances de développement :

   ```bash
   pip install -r requirements-dev.txt
   ```

2. Lancez les tests :
   ```bash
   pytest tests/ -v
   ```

Les tests vérifient :

- La présence et la validité des images
- La structure HTML des pages générées
- L'intégrité du CSS
- Les liens internes
- Le contenu des articles
- La validité des métadonnées
