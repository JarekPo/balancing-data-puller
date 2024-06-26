FROM python:3.9-slim

RUN apt-get update && apt-get install -y cron

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ARG DATABASE_NAME
ARG DATABASE_USER
ARG DATABASE_PASSWORD
ARG DATABASE_HOST
ARG DATABASE_PORT
ARG BRMS_URL

ENV DATABASE_NAME=${DATABASE_NAME}
ENV DATABASE_USER=${DATABASE_USER}
ENV DATABASE_PASSWORD=${DATABASE_PASSWORD}
ENV DATABASE_HOST=${DATABASE_HOST}
ENV DATABASE_PORT=${DATABASE_PORT}
ENV BRMS_URL=${BRMS_URL}

CMD ["python3", "main.py"]
