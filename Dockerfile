# Simple Dockerfile for Railway deployment
FROM python:3.12-slim

WORKDIR /app

# Copy backend code and dependency list
COPY backend/ /app/backend/
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Launch the API server
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8080"]
