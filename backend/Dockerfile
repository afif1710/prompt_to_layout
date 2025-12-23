# backend/Dockerfile
FROM python:3.12-slim AS builder
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /build

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential pkg-config default-libmysqlclient-dev \
    libjpeg-dev zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip wheel --no-cache-dir --wheel-dir /wheels -r requirements.txt

FROM python:3.12-slim AS runtime
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    default-libmysqlclient-dev \
    libjpeg-dev zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

COPY --from=builder /wheels /wheels
RUN pip install --no-cache-dir /wheels/*

COPY . /app

RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser

EXPOSE $PORT

CMD ["sh", "-c", "python3 manage.py migrate && exec gunicorn ui_api.wsgi:application --bind 0.0.0.0:$PORT"]
