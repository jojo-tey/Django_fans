FROM python:3.8.6

RUN pip install --upgrade pip
RUN -m pip install pip==21.1.1

COPY ./djfans/requirements.txt .
RUN pip install -r requirements.txt


COPY ./djfans /djfans

WORKDIR /djfans

COPY ./entrypoint.sh /

ENTRYPOINT ["sh", "/entrypoint.sh"]


