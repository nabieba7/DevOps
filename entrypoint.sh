#!/bin/sh

# Wait for database to be ready (important for Docker Compose)
while ! nc -z db 5432; do
  echo "Waiting for PostgreSQL..."
  sleep 1
done

# Run migrations
python manage.py migrate

# Start development server
exec python manage.py runserver 0.0.0.0:8000