#!/bin/sh

set -e

import os

python manage.py makemigrations
python manage.py migrate --noinput

DJANGO_SUPERUSER_USERNAME=admin \
DJANGO_SUPERUSER_PASSWORD=testpass \
python manage.py createsuperuser --noinput
python manage.py collectstatic --noinput

gunicorn djfans.wsgi:application --bind 0.0.0.0:8000
