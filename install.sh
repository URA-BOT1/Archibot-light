#!/usr/bin/env bash
set -euo pipefail

# Upgrade pip and install dependencies for the backend
python3 -m pip install --upgrade pip
python3 -m pip install -r backend/requirements.txt
