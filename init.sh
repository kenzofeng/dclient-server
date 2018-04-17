#!/usr/bin/env bash
python manage.py makemigrations user
python manage.py migrate
python manage.py createsuperuser