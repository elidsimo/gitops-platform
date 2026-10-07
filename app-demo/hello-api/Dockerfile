FROM python:3.12-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app.py .

FROM base AS test

COPY requirements-dev.txt .
RUN pip install -r requirements-dev.txt

COPY tests ./tests
RUN python -m pytest -q

FROM base AS runtime

RUN useradd --uid 10001 --no-create-home --shell /usr/sbin/nologin appuser

USER 10001

EXPOSE 8080

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--workers", "2", "app:app"]
