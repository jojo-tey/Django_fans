#!/bin/sh

set -e

DJANGO_SUPERUSER_PASSWORD=testpass 
python manage.py createsuperuser --username admin --email admin@email.com --noinput
python manage.py makemigrations
python manage.py migrate --noinput
python manage.py collectstatic --noinput

gunicorn djfans.wsgi:application --bind 0.0.0.0:8000
