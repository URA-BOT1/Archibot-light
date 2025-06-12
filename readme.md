# 🏗️ Archibot-light

> Chatbot IA spécialisé en architecture et urbanisme avec système RAG-LLM intégré

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template/your-template)

## 📋 Description

Archibot-light est un assistant intelligent conçu pour les professionnels de l'architecture et de l'urbanisme. Il utilise la technologie RAG (Retrieval-Augmented Generation) combinée aux LLM pour analyser vos documents et répondre précisément à vos questions techniques.

## ✨ Fonctionnalités

- 🤖 **IA conversationnelle** spécialisée en architecture/urbanisme
- 📚 **Système RAG** pour l'analyse de documents
- 🚀 **API REST** avec endpoints `/chat` et `/health`
- 💾 **Cache Redis** pour les performances
- 🌐 **Interface web** intégrée
- ☁️ **Déploiement facile** sur Railway

## 🚀 Déploiement rapide

### Option 1: Railway (recommandé)

1. **Cliquez sur le bouton "Deploy on Railway"** ci-dessus
2. **Configurez les variables d'environnement** (voir section ci-dessous)
3. **Déployez** - c'est tout !

### Option 2: Local

```bash
# Cloner le projet
git clone https://github.com/votre-username/archibot-light.git
cd archibot-light

# Installer les dépendances
pip install -r requirements.txt

# Lancer le serveur
uvicorn backend.main:app --reload
```

## ⚙️ Configuration

### Variables d'environnement

| Variable | Description | Requis |
|----------|-------------|---------|
| `PORT` | Port du serveur (auto sur Railway) | Non |
| `GROQ_API_KEY` | Clé API Groq | Optionnel |
| `OPENAI_API_KEY` | Clé API OpenAI | Optionnel |
| `TOGETHER_API_KEY` | Clé API Together | Optionnel |

### Configuration Railway

```yaml
# Build Command
pip install -r requirements.txt

# Start Command  
uvicorn backend.main:app --host 0.0.0.0 --port $PORT
```

## 🧪 Test des endpoints

### Vérifier le statut
```bash
curl https://votre-app.railway.app/health
# Réponse: {"status": "ok"}
```

### Poser une question
```bash
curl -X POST https://votre-app.railway.app/chat \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Quelle est la hauteur maximale autorisée en zone urbaine ?"
  }'
```

## 📁 Structure du projet

```
archibot-light/
├── backend/
│   ├── main.py              # Application FastAPI
│   ├── requirements.txt     # Dépendances Python
│   └── models/             # Modèles de données
├── frontend/
│   └── index.html          # Interface web
├── docs/
│   └── api.md              # Documentation API
└── README.md
```

## 🛠️ Utilisation

### Interface web
Accédez à `https://votre-app.railway.app` pour utiliser l'interface graphique.

### API REST
Intégrez directement l'API dans vos applications :

```python
import requests

response = requests.post(
    "https://votre-app.railway.app/chat",
    json={"prompt": "Votre question sur l'architecture"}
)
print(response.json())
```

## 🎯 Cas d'usage

- **Architectes** : Vérification rapide des réglementations
- **Urbanistes** : Analyse des PLU et règles d'urbanisme  
- **Étudiants** : Assistance pour projets et révisions
- **Bureaux d'études** : Automatisation de la veille réglementaire

## 🚧 Roadmap

- [ ] 📤 Upload et traitement de fichiers PDF
- [ ] 🔍 Vectorisation avancée des documents
- [ ] 🔐 Système d'authentification
- [ ] 📊 Interface utilisateur enrichie
- [ ] 🌍 Support multilingue
- [ ] 📈 Analytics et métriques

## 🤝 Contribution

Les contributions sont les bienvenues ! 

1. **Fork** le projet
2. **Créez** votre branche (`git checkout -b feature/nouvelle-fonctionnalite`)
3. **Committez** vos changements (`git commit -m 'Ajout nouvelle fonctionnalité'`)
4. **Push** vers la branche (`git push origin feature/nouvelle-fonctionnalite`)
5. **Ouvrez** une Pull Request

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## 📞 Support

- 🐛 **Issues** : [GitHub Issues](https://github.com/votre-username/archibot-light/issues)
- 📧 **Contact** : votre-email@example.com
- 💬 **Discord** : [Serveur communautaire](https://discord.gg/votre-serveur)

---

<p align="center">
  Fait avec ❤️ pour la communauté architecture & tech
</p>
