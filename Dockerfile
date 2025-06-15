# syntax=docker/dockerfile:1
FROM python:3.11-slim-bookworm

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt gunicorn uvicorn

# Copy project
COPY . .

# Collect static files (if needed, uncomment next line)
# RUN python manage.py collectstatic --noinput

# Expose port (default Django port)
EXPOSE 8000

# Run migrations (optional, for SQLite this is usually not needed in prod)
# CMD ["python", "manage.py", "migrate"]
# Start server using ASGI
CMD ["python", "-m", "uvicorn", "--host", "0.0.0.0", "--port", "8000", "fetures.asgi:application"]
