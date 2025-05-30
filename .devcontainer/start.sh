#!/bin/bash
set -ex
echo "=== Start Script ==="
cd /workspace/backend || exit 1
echo "=== Entered backend ==="
python3 -m venv .venv
echo "=== Created venv ==="
source .venv/bin/activate
pip install -r requirements.txt

# backend 起動
uvicorn main:app --host 0.0.0.0 --port 8000 &
cd /workspace/frontend
pnpm install
pnpm dev