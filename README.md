# django-playground

set up a new django project

# python manage.py makemigrations; python manage.py migrate
create the new django project. Project will be a blank template for the further development

# python manage.py makemigrations; python manage.py migrate
set up the database (sqlite) for local development. makemigrations and migrate should be called everytime when there are changes in the code that correspond to the database

# python manage.py createsuperuser
create a superuser for the admin site of django

# python manage.py runserver
start the webserver.
The project is available at http://localhost:8080
The admin site is available at http://localhost:8080/admin - superuser can login to that page
