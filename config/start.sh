#!/bin/bash

echo installing things
pip3 install -r requirements-dashboard.txt

echo Collecting Static Files
python3 manage.py collectstatic --no-input

echo Migrating
python3 manage.py makemigrations
python3 manage.py migrate

echo Starting Gunicorn
exec gunicorn --config=config/gunicorn.py dashboard.wsgi:application
