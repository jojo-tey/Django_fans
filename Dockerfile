FROM python:3.8.6

RUN pip install --upgrade pip
# RUN apt-get update \
#   && apt-get install -yyq netcat
COPY ./djfans/requirements.txt .


RUN pip install -r requirements.txt

COPY ./djfans /app

WORKDIR /app


COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]
