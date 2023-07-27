
# Introduction.
# Django Setup
Start by creating a new directory for your project and a virtual environment
$ venv/bin/activate
(venv) $ pip install Django
(venv) $ django-admin startproject bulletproof_api .
(venv) $ pip install djangorestframework
(venv) $ python manage.py migrate
(venv) $ python manage.py runserver

# Account App
## Model Manager
## User Model
(venv) $ python manage.py makemigrations
(venv) $ python manage.py migrate
[Error] accounts.UserModel.groups: (fields.E304) Reverse accessor 'Group.user_set' for 'accounts.UserModel.groups' clashes with reverse accessor for 'auth.User.groups'.
[Solution] AUTH_USER_MODEL = "accounts.UserModel"
[Error] django.db.migrations.exceptions.InconsistentMigrationHistory: Migration admin.0001_initial is applied before its dependency accounts.0001_initial on database 'default'.
[Solution] Delete db.sqlite3
(venv) $ python manage.py createsuperuser
http://localhost:8000/admin/login/?next=/admin/
## create some tests
Run all the tests found within the 'animals' package
(venv) $ python manage.py test accounts

# Authentication App
(venv) $ django-admin.exe startapp authentication
(venv) $ pip install django-allauth
(venv) $ python manage.py migrate
(venv) $ python manage.py runserver