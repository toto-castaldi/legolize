#!/bin/sh

cp /app/modules/* /app/src

gunicorn --chdir src --bind 0.0.0.0:5000 --workers 4 --threads 100 wsgi:app