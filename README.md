# Archibot-light Setup Guide

Prérequis
Python 3 (version 3.6 ou supérieure) doit être installé.
(Optionnel, recommandé) Créez un environnement virtuel Python pour isoler les dépendances du projet. Par exemple :
bash
Copier
Modifier
python3 -m venv venv
source venv/bin/activate   # sous Windows : venv\Scripts\activate
Le module venv de Python permet de créer un environnement virtuel (commandée de la forme python -m venv <chemin>)
docs.python.org
.
Installation
Option 1 (script) : exécutez le script d’installation fourni dans le dépôt :
bash
Copier
Modifier
./install.sh
Ce script installe automatiquement les dépendances nécessaires (via pip).
Option 2 (pip) : installez manuellement les dépendances avec pip :
bash
Copier
Modifier
pip install -r requirements.txt
La commande pip install -r requirements.txt installe toutes les bibliothèques listées dans ce fichier
pip.pypa.io
.
Exécution
Option 1 (script) : lancez le script d’exécution :
bash
Copier
Modifier
./run.sh
Ce script démarre le serveur web (il utilise généralement Uvicorn en arrière-plan).
Option 2 (Uvicorn) : démarrez manuellement le serveur FastAPI avec Uvicorn :
bash
Copier
Modifier
uvicorn backend.main:app --reload
Cette commande lance le serveur ASGI en important l’application depuis backend/main.py. L’option --reload active le rechargement automatique du code en cas de modifications. Ce mode de lancement correspond à l’exemple documenté (uvicorn main:app --reload) dans la documentation FastAPI
tutorialspoint.com
.
Le serveur écoute par défaut sur 127.0.0.1:8000. Une fois lancé, l’API est accessible sur http://127.0.0.1:8000 et la documentation interactive Swagger est disponible sur http://127.0.0.1:8000/docs
tutorialspoint.com
.

## Frontend

Une interface web simple est fournie dans le dossier `frontend`.

Vous avez deux options :

1. **Ouvrir `frontend/index.html` directement dans votre navigateur** une fois le backend lancé.

2. **Servir l’interface avec FastAPI** en ajoutant ceci dans votre code backend :

```python
from fastapi.staticfiles import StaticFiles
app.mount('/', StaticFiles(directory='frontend', html=True), name='static')

