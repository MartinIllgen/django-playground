# django-playground

## #1 set up a new django project

### python manage.py makemigrations; python manage.py migrate
create the new django project. Project will be a blank template for the further development.

### python manage.py makemigrations; python manage.py migrate
set up the database (sqlite) for local development. makemigrations and migrate should be called everytime when there are changes in the code that correspond to the database.

### python manage.py createsuperuser
create a superuser for the admin site of django.

### python manage.py runserver
start the webserver.
The project is available at http://localhost:8080
The admin site is available at http://localhost:8080/admin - superuser can login to that page.

## #2 create a new app in the project

### python manage.py startapp events
creates a new app in the project. A blank app template for further development.
Add the new app to INSTALLED_APPS section in settings.py.

## #3 start implementing the app

### creating new models for the app
creating new models in the models.py of the app directory. Run makemigrations and migrate after adding new models to update databaseinformation.

### adding new models to admin site
register new models to admin.py to make them show up in the admin site, superuser can login and add new events or participants.
