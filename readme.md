# EMS Project

## Overview
The EMS Project is a Django-based Employee Management System designed to streamline and manage employee-related data and functionalities. This project aims to provide an efficient and user-friendly interface for handling various aspects of employee management.

## Project Structure

The project structure is organized as follows:

## Command
1. pip install mysqlclient
2. pip install PyMySQL

pip install mysql-python



ems_project/
├── departments/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   ├── migrations/
│   │   └── __init__.py
│   ├── templates/
│   │   └── departments/
│   │       ├── example_template.html  # Example template file
├── users/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   ├── migrations/
│   │   └── __init__.py
│   ├── templates/
│   │   └── users/
│   │       ├── example_template.html  # Example template file
├── ems_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── asgi.py
├── static/
│   ├── admin/
│   │    ├── css/
│   │    ├── js/
│   │    ├── images/
│   │
│   ├── web/
├── templates/
│   ├── admin/ 
│   │    ├── base_site.html <!-- {% include 'layouts/admin.html' %} --> 
│   ├── layouts/ 
│   │    ├── admin.html 
│   ├── partials => hlink.html, header.html, fscript.html, footer.html, 
│        ├── admin/partials => hlink.html, header.html, fscript.html, footer.html, 
│        ├── web/partials => hlink.html, header.html, fscript.html, footer.html, 
│    
├── manage.py
└── readme.md


Add `STATIC_ROOT = BASE_DIR / 'staticfiles'` to settings.py.
Run `python manage.py collectstatic` to collect all static files.