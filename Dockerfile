FROM python:3.8.6

RUN pip install --upgrade pip

COPY ./djfans/requirements.txt .
RUN pip install -r requirements.txt


COPY ./djfans /djfans

WORKDIR /djfans

COPY ./entrypoint.sh /

ENTRYPOINT ["sh", "/entrypoint.sh"]


