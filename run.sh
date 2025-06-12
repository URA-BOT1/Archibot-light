#!/usr/bin/env bash
set -euo pipefail

# Start Redis if available
if command -v redis-server >/dev/null 2>&1; then
  echo "Starting redis-server..."
  redis-server --daemonize yes
else
  echo "redis-server not found; continuing without it." >&2
fi

# Launch the FastAPI app using uvicorn
exec uvicorn backend.main:app --host 0.0.0.0 --port "${PORT:-8000}"
