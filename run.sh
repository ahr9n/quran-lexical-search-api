#!/bin/bash

# Install requirements
pip install -r requirements.txt

# Create new migrations based on the changes in models
python3 manage.py makemigrations

# Apply the migrations to the database
python3 manage.py migrate

# Create a superuser to be able to use Django Admin Interface
python3 manage.py createsuperuser

# Visit the site
xdg-open http://localhost:8000

# Run the app locally
python3 manage.py runserver
