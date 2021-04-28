#!/bin/sh



python manage.py makemigrations --settings=djfans.prod
python manage.py migrate --settings=djfans.prod --noinput
python manage.py collectstatic --settings=djfans.prod --noinput

gunicorn djfans.wsgi:application --bind 0.0.0.0:8000
