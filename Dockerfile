
FROM python:3.11-slim

WORKDIR /app

# Copy and install requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all files
COPY . .

# Set Python path
ENV PYTHONPATH=/app

# Railway uses this port variable
EXPOSE ${PORT:-8000}

# Start the app with correct module path
CMD uvicorn backend.main:app --host 0.0.0.0 --port ${PORT:-8000}
