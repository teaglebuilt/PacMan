FROM python:3.7-slim as base

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PIP_NO_BINARY psycopg2
ENV APP_SETTINGS=configs.DockerConfig

WORKDIR /usr/src

COPY . .


RUN apt-get update \
    && apt-get install -y libpq-dev gcc \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --upgrade pip

RUN pip install -r requirements.txt


EXPOSE 8000


CMD ["gunicorn", "--access-logfile", "docker.logs", "--workers=2", "-b0.0.0.0:5000", "wsgi:app"]


############ START NEW IMAGE:  DEBUGGER ######################
FROM base as debug 

RUN pip install ptvsd

WORKDIR  /usr/src

CMD python -m ptvsd --host 0.0.0.0 --port 5678 --wait --multiprocess -m flask run -h 0.0.0.0 -p 5000