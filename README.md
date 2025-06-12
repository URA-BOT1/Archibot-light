Archibot-light Setup Guide
Prerequisites
Python 3.6 or higher
Recommended: create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate   # on Windows: venv\Scripts\activate
Installation
Install the dependencies from `requirements.txt`:
```bash
pip install -r requirements.txt
```
Running the Backend
Start the FastAPI server with Uvicorn:
```bash
uvicorn backend.main:app --reload
```
This command launches the ASGI server and imports the app from backend/main.py.
The --reload option enables auto-reload on file changes.

By default the backend uses OpenAI for language generation. If the
`OPENAI_API_KEY` variable is missing, it will try Groq first and then
Together.ai provided their keys are set.

Once running:

API available at: http://127.0.0.1:8000

Swagger UI docs at: http://127.0.0.1:8000/docs

Frontend Usage
A simple web interface is provided in the frontend directory.

You can either:

Open frontend/index.html directly in your browser

Or serve it via FastAPI with:
```python
from fastapi.staticfiles import StaticFiles
app.mount("/", StaticFiles(directory="frontend", html=True), name="static")
```
Then open http://127.0.0.1:8000 to interact with the /chat endpoint.

If the frontend and backend are deployed separately, set the backend's
URL for the JavaScript client. Define a `BACKEND_URL` environment
variable during your build or include a script tag before `app.js` that
sets `window.BACKEND_URL`:

```html
<script>
  window.BACKEND_URL = 'https://your-backend.example.com';
</script>
```

Health Check
You can confirm the backend is running by executing:
```bash
curl http://127.0.0.1:8000/health
```
Running Tests
Run unit tests using:
```bash
pytest
```
Environment Variables
The application relies on several environment variables when deployed.
An example configuration is provided in `.env.example`.

PORT – port for the server (default: 8000)

OPENAI_API_KEY – API key for OpenAI

GROQ_API_KEY, TOGETHER_API_KEY – keys for external LLMs
  When no OpenAI key is provided, the backend will try Groq first and
  then Together.ai if their keys are present.


BACKEND_URL – base URL for the chat backend when the frontend is served separately

Set these variables in your Railway project or local environment using a `.env` file or by exporting them in your shell.

Deployment on Railway
---------------------

The project can be deployed on [Railway](https://railway.app) using its
Nixpacks builder. The included `railway.toml` configures the build and
start command:

```toml
[build]
  builder = "Nixpacks"

[deploy]
  startCommand = "uvicorn backend.main:app --host 0.0.0.0 --port $PORT"
```

Running `railway up` will build the service with Nixpacks and launch the
API on the port provided by Railway.
