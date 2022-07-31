FROM fedora/python:latest

LABEL AUTHOR="OTUOZE"

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

COPY ./requirements.txt .

RUN pip install python3-gdal
RUN pip install -r /requirements.txt


COPY . .

RUN adduser -D user
USER user
