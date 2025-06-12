# Multi-stage build
FROM python:3.11-slim AS builder
WORKDIR /app
COPY backend/requirements.txt ./backend/requirements.txt
RUN pip install --prefix=/install -r backend/requirements.txt

FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /install /usr/local
COPY . .
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8080"]
