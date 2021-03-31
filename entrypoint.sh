#!/bin/sh

python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --no-input

gunicorn djfans.wsgi:application --bind 127.0.0.1:8000



