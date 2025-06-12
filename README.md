🏗️ Archibot-light

Chatbot IA spécialisé en architecture et urbanisme avec système RAG-LLM intégré


Archibot-light est un assistant intelligent conçu pour les professionnels de l'architecture et de l'urbanisme. Il utilise la technologie RAG (Retrieval-Augmented Generation) combinée aux LLM pour analyser vos documents et répondre précisément à vos questions techniques.
✨ Fonctionnalités

🤖 IA conversationnelle spécialisée en architecture/urbanisme
📚 Système RAG pour l'analyse de documents
🚀 API REST avec endpoints /chat et /health
💾 Cache Redis pour les performances
🌐 Interface web intégrée
☁️ Déploiement facile sur Railway

🚀 Déploiement rapide
Option 1: Railway (recommandé)

Cliquez sur le bouton "Deploy on Railway" ci-dessus
Configurez les variables d'environnement (voir section ci-dessous)
Déployez - c'est tout !

Option 2: Local
bash# Cloner le projet
git clone https://github.com/votre-username/archibot-light.git
cd archibot-light

# Installer les dépendances
pip install -r requirements.txt

# Lancer le serveur
uvicorn backend.main:app --reload
⚙️ Configuration
Variables d'environnement
VariableDescriptionRequisPORTPort du serveur (auto sur Railway)NonGROQ_API_KEYClé API GroqOptionnelOPENAI_API_KEYClé API OpenAIOptionnelTOGETHER_API_KEYClé API TogetherOptionnel
Configuration Railway
yaml# Build Command
pip install -r requirements.txt

# Start Command  
uvicorn backend.main:app --host 0.0.0.0 --port $PORT
🧪 Test des endpoints
Vérifier le statut
bashcurl https://votre-app.railway.app/health
# Réponse: {"status": "ok"}
Poser une question
bashcurl -X POST https://votre-app.railway.app/chat \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Quelle est la hauteur maximale autorisée en zone urbaine ?"
  }'
📁 Structure du projet
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
🛠️ Utilisation
Interface web
Accédez à https://votre-app.railway.app pour utiliser l'interface graphique.
API REST
Intégrez directement l'API dans vos applications :
pythonimport requests

response = requests.post(
    "https://votre-app.railway.app/chat",
    json={"prompt": "Votre question sur l'architecture"}
)
print(response.json())
🎯 Cas d'usage

Architectes : Vérification rapide des réglementations
Urbanistes : Analyse des PLU et règles d'urbanisme
Étudiants : Assistance pour projets et révisions
Bureaux d'études : Automatisation de la veille réglementaire

🚧 Roadmap

 📤 Upload et traitement de fichiers PDF
 🔍 Vectorisation avancée des documents
 🔐 Système d'authentification
 📊 Interface utilisateur enrichie
 🌍 Support multilingue
 📈 Analytics et métriques

🤝 Contribution
Les contributions sont les bienvenues !

Fork le projet
Créez votre branche (git checkout -b feature/nouvelle-fonctionnalite)
Committez vos changements (git commit -m 'Ajout nouvelle fonctionnalité')
Push vers la branche (git push origin feature/nouvelle-fonctionnalite)
Ouvrez une Pull Request

📄 Licence
Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.
📞 Support

🐛 Issues : GitHub Issues
📧 Contact : votre-email@example.com
💬 Discord : Serveur communautaire
