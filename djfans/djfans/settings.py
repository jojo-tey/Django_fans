"""
Django settings for djfans project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""


from pathlib import Path
import os
# import keys


BASE_DIR = Path(__file__).resolve().parent.parent
ROOT_DIR = os.path.dirname(BASE_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!


# Django-local
# key for test = '-nro!j**h$!c=d(*r30+u46g$^(oge1!*9ymb4v8ks9%mwyim%'
# SECRET_KEY = '-nro!j**h$!c=d(*r30+u46g$^(oge1!*9ymb4v8ks9%mwyim%'
# SECRET_KEY = keys.SECRET
# DEBUG = True
# ALLOWED_HOSTS = []

# Docker
SECRET_KEY = os.environ['SECRET_KEY']
DEBUG = os.environ['DEBUG']
ALLOWED_HOSTS = ['*']


# SECURITY WARNING: don't run with debug turned on in production!


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'authy',
    'tier',
    'post',
    'comment',
    'notifications',
    'direct',
    'storages',

    # Social login
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'django.contrib.sites',
    # provider
    'allauth.socialaccount.providers.google',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'djfans.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'djfans/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'authy.views.SideNavInfo',
            ],
        },
    },
]

WSGI_APPLICATION = 'djfans.wsgi.application'


# Database Local
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# Postgresql
# DATABASES = keys.default

# Sqlite3
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# DB AWS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': os.environ['DB_HOST'],
        'PORT': '5432',
        'NAME': os.environ['DB_NAME'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASSWORD']
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
# Local, use pipeline when DEBUG=True

# for dev

# STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(ROOT_DIR, 'static')
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'djfans/static'),
# ]

# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# for S3 bucket - deploy

# AWS Setting
AWS_STORAGE_BUCKET_NAME = 'djfans-static'
AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_KEY']
AWS_REGION = os.environ['AWS_REGION']
S3_ACCESS_KEY = os.environ['S3_ACCESS_KEY']
AWS_DEFAULT_ACL = 'public-read'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.%s.amazonaws.com' % (
    AWS_STORAGE_BUCKET_NAME, AWS_REGION)

AWS_S3_MAX_MEMORY_SIZE = 1024000000  # value in bytes 1GB here

# Static Setting
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'djfans/static'),
]
STATICFILES_STORAGE = STATICFILES_STORAGE = 'storages.backends.s3boto3.S3StaticStorage'

# Media Setting
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'


# Auth

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

SITE_ID = 1

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = 'login'
LOGIN_URL = '/user/login/'
