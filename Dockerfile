FROM python:3.8-buster
# Installing build dependencies
RUN apt-get update && apt-get -y install  musl-dev python3-dev musl-dev bash libpq-dev libpq-dev postgresql postgresql-contrib gcc

COPY . /app
WORKDIR /app

RUN chmod 777 -R /app
RUN chmod +x /app/dev.sh

RUN pip install --upgrade pip && pip install pytest psycopg2 cython && pip install poetry && poetry install

EXPOSE 8000
