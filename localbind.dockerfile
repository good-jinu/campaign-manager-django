FROM python:3.9.16

ENV PYTHONUNBUFFERED 1

copy . /app

WORKDIR /app

RUN apt-get update

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

EXPOSE 8000