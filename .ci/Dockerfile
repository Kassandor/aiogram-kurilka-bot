# Install uv
FROM python:3.11-alpine AS builder
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Ставим зависимости в системный python контейнера
ENV UV_PROJECT_ENVIRONMENT=/usr/local

WORKDIR /app

# Установка зависимостей с кэшированием
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --locked --no-install-project --no-editable

FROM python:3.11-alpine

# Копируем только зависимости + бинарники
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

WORKDIR /app

# Копируем только source проекта
COPY kurilka_bot/ ./kurilka_bot

# Копируем entrypoint.sh, даем права на запуск
COPY .ci/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]