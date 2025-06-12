# Archibot-light Setup Guide

## Prerequisites
* Python 3.6 or higher
* **Recommended:** create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate   # on Windows: venv\Scripts\activate
Installation
Install the dependencies from backend/requirements.txt:

bash
Copier
Modifier
pip install -r backend/requirements.txt
Running the Backend
Start the FastAPI server with Uvicorn:

bash
Copier
Modifier
uvicorn backend.main:app --reload
This command launches the ASGI server and imports the app from backend/main.py.
The --reload option enables auto-reload on file changes.

Once running:

API available at: http://127.0.0.1:8000

Swagger UI docs: http://127.0.0.1:8000/docs

Frontend Usage
A simple web interface is provided in the frontend directory.

You can either:

Open frontend/index.html directly in your browser.

Serve it via FastAPI with:

python
Copier
Modifier
from fastapi.staticfiles import StaticFiles
app.mount("/", StaticFiles(directory="frontend", html=True), name="static")
Then open http://127.0.0.1:8000 to interact with the /chat endpoint.

Health Check
You can confirm the backend is running by executing:

bash
Copier
Modifier
curl http://127.0.0.1:8000/health
Running Tests
Run unit tests using:

bash
Copier
Modifier
pytest
yaml
Copier
Modifier

---

### ✅ À faire maintenant :

1. Ouvre ton `README.md` (dans GitHub ou Codex)
2. **Remplace tout par ce contenu**
3. Puis fais :

```bash
git add README.md
git commit -m "✅ README.md nettoyé et corrigé"
git push