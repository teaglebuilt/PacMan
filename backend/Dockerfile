FROM python:3.7

WORKDIR /usr/src

COPY . .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

EXPOSE 8000

CMD ["gunicorn", "--access-logfile", "docker.logs", "--workers=2", "-b0.0.0.0:5000", "wsgi:app"]