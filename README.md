Archibot-light Setup Guide
Prerequisites
Python 3.6 or higher
Recommended: create and activate a virtual environment
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

Swagger UI docs at: http://127.0.0.1:8000/docs

Frontend Usage
A simple web interface is provided in the frontend directory.

You can either:

Open frontend/index.html directly in your browser

Or serve it via FastAPI with:

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
Environment Variables
The application relies on several environment variables when deployed.
An example configuration is provided in .env.example.

PORT – port for the server (default: 8080)

REDIS_URL – address of the Redis instance used by the backend

OPENAI_API_KEY – API key for optional OpenAI integration

GROQ_API_KEY, TOGETHER_API_KEY – for external LLMs

UPSTASH_REDIS_REST_URL, UPSTASH_REDIS_REST_TOKEN – credentials if using Upstash Redis

Set these variables in your Railway project or local