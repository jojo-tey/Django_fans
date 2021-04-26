#!/bin/sh

set -e

import os

python manage.py makemigrations
python manage.py migrate --noinput

python manage.py createcachetable

if ['$DJANGO_SUPERUSER_USERNAME']
then
    python manage.py createsuperuser \
        --noinput \
        --username ['$DJANGO_SUPERUSER_USERNAME'] \
        --email ['$DJANGO_SUPERUSER_USERNAME']
fi



python manage.py collectstatic --noinput

gunicorn djfans.wsgi:application --bind 0.0.0.0:8000
