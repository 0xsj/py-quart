# Use the official Python base image
FROM python:3.11 AS build-env

# Poetry TODO:
ARG POETRY_VERSION=1.3.2
ARG PORT

# Install deps
RUN pip3 install --upgrade pip && \
  pip3 install poetry==$POETRY_VERSION && \
  poetry install --without dev

# Runtime
