
FROM python:3.8-alpine

ENV PATH="/scripts:${PATH}"


COPY ./djfans/requirements.txt /requirements.txt 
RUN apk add --update --no-cache --virtual .tmp python3-dev gcc libc-dev build-base linux-headers 
RUN apk add --no-cache jpeg-dev zlib-dev

RUN pip install cryptography
RUN pip install -r /requirements.txt
RUN apk del .tmp

RUN mkdir /djfans
COPY ./djfans /djfans
WORKDIR /djfans
COPY ./scripts /scripts



RUN chmod +x /scripts/*

# access permission for user
RUN mkdir -p /vol/web/media  
RUN mkdir -p /vol/web/static

RUN adduser -D user
RUN chown -R user:user /vol
RUN chmod -R 755 /vol/web
USER user

CMD ["entrypoint.sh"]