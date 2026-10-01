# TaskFlow

A task management REST API built with FastAPI, while learning backend development.

## Progress

- [x] Day 1 — Project setup, first endpoint
- [ ] Day 2 — Query and path parameters
- [ ] Day 3 — Request body, CRUD
- [ ] Day 4 — Pydantic schemas
...

## Stack

- FastAPI
- Pydantic v2
- SQLAlchemy 2.0 (async) + PostgreSQL
- Alembic
- pytest

## Run locally

\`\`\`bash
python -m venv .venv
source .venv/bin/activate
pip install "fastapi[standard]"
fastapi dev app/main.py
\`\`\`