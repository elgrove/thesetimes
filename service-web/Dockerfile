FROM python:3.9-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# Install poetry separated from system interpreter
ENV POETRY_VERSION=1.4.0
ENV POETRY_VENV=/opt/poetry-venv
RUN python3 -m venv $POETRY_VENV \
    && $POETRY_VENV/bin/pip install -U pip setuptools \
    && $POETRY_VENV/bin/pip install poetry==${POETRY_VERSION}

# Add `poetry` to PATH
ENV PATH="${PATH}:${POETRY_VENV}/bin"
ENV POETRY_CACHE_DIR=/opt/.cache

RUN mkdir -p /usr/src/package-orm
WORKDIR /usr/src/package-orm
COPY package-orm /usr/src/package-orm

WORKDIR /usr/src/app
COPY service-web/poetry.lock service-web/pyproject.toml ./
RUN poetry check
RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-cache --without dev

COPY service-web /usr/src/app

CMD ["poetry", "run", "gunicorn", "-w", "1", "-b", "0.0.0.0", "main:create_app()"]