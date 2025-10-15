FROM python:3.12-slim

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN pip install poetry --no-cache-dir

COPY pyproject.toml poetry.lock /.

RUN poetry install --no-cache --without develop --no-root

COPY ./app .
