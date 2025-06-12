# 🧠 Archibot-light — Chatbot IA RAG-LLM

Assistant intelligent pour l’architecture et l’urbanisme.  
Capable d'ingérer vos documents et de répondre à vos questions grâce à un système de **RAG** (Retrieval-Augmented Generation) et des **LLM** comme GPT ou Groq.

---

## 🚀 Fonctionnalités

✅ IA conversationnelle spécialisée  
✅ Endpoint `/chat` intelligent (LLM + Redis)  
✅ Endpoint `/health` pour vérifier le statut  
✅ Prêt à déployer sur **Railway** (backend + Redis)  
✅ Frontend web minimal intégré (`StaticFiles`)

---

## ⚙️ Déploiement (Railway recommandé)

### 🧱 Build settings Railway

- **Builder** : `Nixpacks` *(ou Railway Build bêta)*
- **Build command** :
  ```bash
  pip install -r requirements.txt
Start command :

bash
Copier
Modifier
uvicorn backend.main:app --host 0.0.0.0 --port $PORT
🔐 Variables d’environnement à définir
Clé	Exemple / Source
PORT	8000 (géré automatiquement par Railway)
GROQ_API_KEY	(facultatif, pour moteur Groq)
OPENAI_API_KEY	(facultatif, pour moteur OpenAI)
TOGETHER_API_KEY	(optionnel)

🧪 Tester les endpoints
➤ Vérifier le serveur :
bash
Copier
Modifier
curl https://<ton-app>.railway.app/health
# ↪︎ {"status": "ok"}
➤ Parler au bot :
bash
Copier
Modifier
curl -X POST https://<ton-app>.railway.app/chat \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Quelle hauteur maximale en zone U ?"}'
🛠 Arborescence minimale
bash
Copier
Modifier
backend/
  ├── main.py            # App FastAPI
  ├── requirements.txt   # Dépendances
frontend/
  └── index.html         # Interface web (optionnelle)
🧠 Ce projet est fait pour :
Les développeurs back souhaitant intégrer des LLM dans un vrai use case

Les architectes/urbanistes qui veulent automatiser la veille réglementaire

Toute personne qui veut tester un chatbot RAG simple et auto-hébergeable

📦 À venir (TODO)
Upload de fichiers

Vectorisation des documents

Authentification

Interface UI plus complète

🤝 Contribuer
Fork, clone, propose un PR — ou contacte-moi pour en discuter.

yaml
Copier
Modifier

---

Tu veux que je te le commit direct dans ton repo avec un lien `Deploy on Railway` et badge de build ?





