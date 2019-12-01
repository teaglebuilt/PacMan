#!/bin/sh
source env/bin/activate
exec gunicorn -b :5000 --access-logfile - run:application