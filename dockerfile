# Dockerfile optimized for SkyLearn's requirements structure
FROM python:3.10-slim-bullseye

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    postgresql-client \
    gcc \
    python3-dev \
    libpq-dev \
    libjpeg-dev \
    zlib1g-dev && \
    rm -rf /var/lib/apt/lists/*

# Copy requirements directory
COPY requirements ./requirements

# Install Python dependencies - try different requirement files
RUN pip install --upgrade pip setuptools wheel && \
    if [ -f requirements/local.txt ]; then \
        pip install -r requirements/local.txt; \
    elif [ -f requirements/base.txt ]; then \
        pip install -r requirements/base.txt; \
    elif [ -f requirements.txt ]; then \
        pip install -r requirements.txt; \
    else \
        echo "Installing default Django packages" && \
        pip install Django psycopg2-binary Pillow gunicorn whitenoise python-decouple; \
    fi

# Copy project files
COPY . .

# Create necessary directories
RUN mkdir -p static media

# Collect static files (may fail if DEBUG=False, that's ok)
RUN python manage.py collectstatic --noinput || true

# Expose port
EXPOSE 8000

# Startup command
CMD python manage.py migrate && \
    python manage.py runserver 0.0.0.0:8000