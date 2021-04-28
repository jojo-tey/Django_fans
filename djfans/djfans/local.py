from .settings import *


# Running env - Local

SECRET_KEY = '-nro!j**h$!c=d(*r30+u46g$^(oge1!*9ymb4v8ks9%mwyim%'
DEBUG = True
ALLOWED_HOSTS = []


# Database - Sqlite3

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# static setting

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(ROOT_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'djfans/static'),
]


# media setting

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
