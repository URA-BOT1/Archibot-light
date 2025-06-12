# Archibot-light Setup Guide

## Prerequisites
* Python 3.6 or higher
* **Recommended:** create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate   # on Windows: venv\Scripts\activate
```

## Installation
Install the dependencies from `backend/requirements.txt`:

```bash
pip install -r backend/requirements.txt
```

## Running
Start the FastAPI server with Uvicorn:

```bash
uvicorn backend.main:app --reload
```

The API is available at http://127.0.0.1:8000 and the interactive docs at http://127.0.0.1:8000/docs
