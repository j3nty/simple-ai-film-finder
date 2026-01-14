# simple-ai-film-finder-ollama

A simple Django project that provides watch-based suggestions (recommendations) based on what you’ve watched.
It uses a local Ollama server for AI-powered suggestion generation.
It also includes registration with email confirmation using a local SMTP server for development/testing, and uses `django-allauth` for authentication flows.

## Features
- Suggestions based on watch history (AI-assisted via Ollama).
- Registration with email confirmation (local SMTP).
- Authentication/registration via `django-allauth`.

## Requirements
- Docker installed and running.
- Docker Compose v2 (`docker compose`).
- Existing Ollama reachable on `http://localhost:11434` (published to the host).

## Start
```bash
docker compose up --build
```

Open: http://localhost

## Stop
```bash
docker compose down
```

## Logs
```bash
docker compose logs -f
```

## Ollama connection
Default env: `OLLAMA_HOST=http://host.docker.internal:11434`
