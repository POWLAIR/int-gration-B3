# Vivre aux Lilas

## Introduction

Ce projet génère un site web statique à partir de fichiers Markdown et CSV. Il utilise Python pour le traitement des fichiers et Jinja2 pour le templating. Les pages générées incluent des articles avec des images associées et une page de membres.

## Prérequis Systèmes

- **Système d'exploitation** : Linux (Ubuntu recommandé)
- **Python** : Version 3.12 ou supérieure
- **Pip** : Gestionnaire de paquets Python
- **Modules Python** : `markdown`, `jinja2`

## Installation sur Linux

1. **Installer Python et Pip** :

   ```bash
   sudo apt update
   sudo apt install python3 python3-pip
   ```

2. **Installer les modules Python requis** :
   ```bash
   pip install markdown jinja2
   ```

## Commandes de Build

Pour générer le site, utilisez le script `generate.py` :

1. **Exécuter le script de génération** :

   ```bash
   python script/generate.py chemin/vers/dossier_entree
   ```

   - `chemin/vers/dossier_entree` : Le chemin vers le dossier contenant les fichiers Markdown et CSV.

## Options et Commandes

- **Aucun argument supplémentaire** : Le script prend un seul argument, le chemin vers le dossier d'entrée.
- **Structure des fichiers** : Assurez-vous que les fichiers Markdown suivent le format `YYYY-MM-DD-nom-evenement.md` et que les images correspondantes sont nommées `nom-evenement.webp` dans le dossier `ressource`.

## Membres du Groupe

- Prénom1 N.
- Prénom2 N.
- Prénom3 N.

## Notes

- Les images doivent être placées dans le dossier `ressource` et doivent correspondre aux événements décrits dans les fichiers Markdown.
- Un placeholder est utilisé si aucune image spécifique n'est trouvée pour un article.
- Le site généré est statique et ne nécessite pas de serveur pour être consulté.
