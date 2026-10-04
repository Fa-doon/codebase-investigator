# Codebase Investigator

An AI-powered tool for investigating and understanding a codebase using semantic search and LLMs.

## Stack

- Python
- FastAPI
- PostgreSQL
- pgvector

## Current Status

Early development.

## Run Locally

Create and activate the virtual environment:

```bash
python -m venv .venv
source .venv/Scripts/activate
```

Install dependencies:

```bash
pip install fastapi uvicorn
```

Start the server:

```bash
uvicorn app.main:app --reload
```

## API documentation:

- http://127.0.0.1:8000/docs
- http://127.0.0.1:8000/redoc