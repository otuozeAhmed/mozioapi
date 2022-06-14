FROM python:3.10-alpine

LABEL AUTHOR="OTUOZE"

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev
RUN apk add -y python-gdal
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps


WORKDIR .
COPY . .

RUN adduser -D user
USER user