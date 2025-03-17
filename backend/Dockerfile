# syntax=docker/dockerfile:1
FROM python:3.9-slim AS base
WORKDIR /app
ENV PYTHONUNBUFFERED=1 \
    PIPENV_VENV_IN_PROJECT=1
RUN pip install --no-cache-dir pipenv

RUN adduser --disabled-password --gecos "" --uid 1001 api

# --- development for local ---
FROM base AS development
COPY Pipfile Pipfile.lock ./
RUN pipenv install --dev
COPY . .
EXPOSE 3002
CMD ["pipenv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]


# --- builder ---
FROM base AS builder
COPY Pipfile Pipfile.lock ./
RUN pipenv install --deploy
COPY . .
USER api
COPY --chown=api:api . .

# --- Production Stage ---
FROM base AS production
COPY --chown=api:api --from=builder /app /app
WORKDIR /app
USER api
CMD ["pipenv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]