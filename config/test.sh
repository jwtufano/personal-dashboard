#!/bin/bash

echo Collecting Static Files
python3 manage.py collectstatic --no-input

echo Migrating
python3 manage.py makemigrations
python3 manage.py migrate

echo Starting Tests
python3 manage.py test
