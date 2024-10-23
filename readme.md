# Vivre aux lilas - Site web de l'association

Ce projet est un site web statique pour l'association de quartier "Vivre aux lilas".

## Prérequis système

- Node.js (version 14.0.0 ou supérieure)
- npm (généralement installé avec Node.js)
- Un navigateur web moderne

## Installation sur Windows

1. Installer Node.js :
   - Télécharger la dernière version LTS de Node.js depuis https://nodejs.org/
   - Suivre les instructions d'installation par défaut

2. Vérifier l'installation de Node.js et npm :
   - Ouvrir PowerShell et exécuter :
     ```
     node --version
     npm --version
     ```

3. Cloner le dépôt :
   ```
   git clone https://github.com/votre-utilisateur/vivreauxlilas.git
   cd vivreauxlilas
   ```

4. Installer les dépendances :
   ```
   npm install
   ```

## Structure du projet

```
vivreauxlilas/
├── src/
│   ├── index.html
│   ├── actualites.html
│   ├── membres.html
│   ├── css/
│   │   └── main.css
│   └── js/
│       └── main.js
├── data/
│   ├── actualites.json
│   └── membres.json
├── scripts/
│   └── build.js
└── package.json
```

## Build et génération du site

1. Générer le site :
   ```
   npm run build
   ```

2. Le site généré sera disponible dans le dossier `dist/`.

3. Pour servir le site localement :
   ```
   npm run serve
   ```
   Le site sera accessible à l'adresse http://localhost:8080/

## Commandes npm

- `npm run build` : Génère le site
- `npm run serve` : Lance un serveur de développement local
- `npm run watch` : Surveille les changements et régénère le site automatiquement

## Membres du groupe

- Jean D.
- Marie L.
- Pierre B.
