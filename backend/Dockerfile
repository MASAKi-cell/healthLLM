# syntax=docker/dockerfile:1
FROM python:3.9-slim
WORKDIR /app


# --- development for local ---
FROM base AS development
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
EXPOSE 3002
CMD ["python", "app/main.py"]



# --- builder ---
    FROM base AS builder





# --- Production Stage ---
FROM base AS production