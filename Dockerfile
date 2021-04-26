FROM python:3.8.6

RUN pip install --upgrade pip


COPY ./djfans/requirements.txt .
RUN pip install -r requirements.txt


COPY ./djfans /djfans

WORKDIR /djfans

COPY ./entrypoint.sh /

RUN python -c "import django; django.setup(); \
  from django.contrib.auth.management.commands.createsuperuser import get_user_model; \
  get_user_model()._default_manager.db_manager('$DB_NAME').create_superuser( \
  username='$DJANGO_SUPERUSER_USERNAME', \
  email='$DJANGO_SUPERUSER_EMAIL', \
  password='$DJANGO_SUPERUSER_PASSWORD')"


ENTRYPOINT ["sh", "/entrypoint.sh"]


