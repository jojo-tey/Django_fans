#!/bin/sh



python manage.py makemigrations --settings=djfans.prod
python manage.py migrate --settings=djfans.prod
python manage.py collectstatic --settings=djfans.prod

gunicorn djfans.wsgi:application --bind 0.0.0.0:8000
