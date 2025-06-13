FROM python:3.11-slim

WORKDIR /app

# Copy and install requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all application code
COPY . .

# Railway will set PORT
EXPOSE ${PORT:-8000}

# Start the application
CMD uvicorn backend.main:app --host 0.0.0.0 --port ${PORT:-8000}
