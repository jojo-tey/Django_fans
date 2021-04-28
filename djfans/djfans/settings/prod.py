from .base import *


# Running env - Docker

SECRET_KEY = os.environ['SECRET_KEY']
DEBUG = os.environ['DEBUG']
ALLOWED_HOSTS = ['*']


# Database - AWS RDS

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
STATIC_ROOT = os.path.join(ROOT_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'djfans/static'),
]
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3StaticStorage'

# Media Setting
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
