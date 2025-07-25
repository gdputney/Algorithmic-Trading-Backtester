# Stage 1: Base image with Python
FROM python:3.12-slim-bullseye AS base

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

# Install system dependencies (required for pandas/yfinance)
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# ----------------------------------------
# Stage 2: Builder for dependencies
FROM base AS builder

WORKDIR /app

# Install pip requirements first (caching layer)
COPY requirements.txt .
RUN pip install --user -r requirements.txt

# ----------------------------------------
# Stage 3: Final lightweight image
FROM base AS runtime

WORKDIR /app

# Copy installed packages from builder
COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH

# Copy application code
COPY . .

# Data volume (optional)
VOLUME /app/data /app/results

# Entry point
CMD ["python", "main.py"]