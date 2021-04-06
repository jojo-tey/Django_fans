FROM python:3.8

RUN pip install --upgrade pip

COPY ./djfans/requirements.txt .
RUN pip install -r requirements.txt

COPY ./djfans /app

WORKDIR /app

COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]
