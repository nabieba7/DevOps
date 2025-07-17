#!/bin/sh

echo "Waiting for database to be ready..."
while ! nc -z $DATABASE_HOST 5432; do
  sleep 1
done
echo "Database is ready."

# Run migrations
python manage.py migrate

# Start development server
exec python manage.py runserver 0.0.0.0:8000