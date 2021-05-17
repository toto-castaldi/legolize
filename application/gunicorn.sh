#!/bin/sh
gunicorn --chdir src --bind 0.0.0.0:5000 -w 2 --threads 2 wsgi:app