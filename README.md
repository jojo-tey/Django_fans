# Djfans

- Personal project for Onlyfans clone

### Used skill
- Django
- Docker-compose
- Terraform 
- Jenkins



### Test command

1. git clone https://github.com/jojo-tey/Django_fans.git
2. cd Django_fans/djfans
3. Disable product part in settings.py 
```
########################################
# Disable this part for local running

# Running env - Docker

SECRET_KEY = os.environ['SECRET_KEY']
DEBUG = os.environ['DEBUG']
ALLOWED_HOSTS = ['*']
########################################
```
4. python manage.py makemigrations --settings=djfans.local
5. python manage.py migrate --settings=djfans.local
6. python manage.py runserver --settings=djfans.local


