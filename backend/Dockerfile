FROM python:3.7-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PIP_NO_BINARY psycopg2

WORKDIR /usr/src

COPY . .


RUN apt-get update \
    && apt-get install -y libpq-dev gcc \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --upgrade pip

RUN pip install -r requirements.txt


EXPOSE 8000


CMD ["gunicorn", "--access-logfile", "docker.logs", "--workers=2", "-b0.0.0.0:5000", "wsgi:app"]