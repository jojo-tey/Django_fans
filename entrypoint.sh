#!/bin/sh

set -e

python manage.py createsuperuser --noinput
python manage.py makemigrations
python manage.py migrate --noinput
python manage.py collectstatic --noinput

gunicorn djfans.wsgi:application --bind 0.0.0.0:8000
