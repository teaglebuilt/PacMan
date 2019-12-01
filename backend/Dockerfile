FROM python:3.7-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PIP_NO_BINARY psycopg2
ENV FLASK_SKIP_DOTENV 1
ENV FLASK_APP run.py

WORKDIR /src

ADD requirements.txt requirements.txt

RUN apt-get update \
    && apt-get install -y libpq-dev gcc \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . /src

EXPOSE 5000

ENTRYPOINT ["./boot.sh"]