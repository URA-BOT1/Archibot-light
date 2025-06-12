#!/bin/bash
cd "$(dirname "$0")"
pip install -r backend/requirements.txt
uvicorn backend.main:app --host 0.0.0.0 --port ${PORT:-8080}
