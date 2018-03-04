# REST-API
A REST API developed in Django REST Framework.
# Getting Started
These instructions will get you a copy of the project up and running on your local machine.
# Prerequisites
This project has requirements file. You are required to install all requirements before starting this project.
To install all requirements use following command in a python 2.7 supported virtual environment.
pip install -r requirements.txt
Go in to the repository
cd rest/

This API uses authentication so first create a superuser.
django-admin createsuperuser

Now, start a development server by typing
./manage.py runserver
To get a token, Send a POST request with username and passoword as parameters.
http://127.0.0.1:8000/api-token-auth/
This will return auth token.
Use this token as Header in all POST/PUT requests.
example of using Header
key: Authorization   value: Token 0e401dc655b79eb248db9f7d6c004e6092b8d39c
To view all clients:
GET: http://127.0.0.1:8000/clients
To view single clients:
GET: http://127.0.0.1:8000/clients/1
To create a client:
POST: http://127.0.0.1:8000/clients/create/
To update a client
PUT: http://127.0.0.1:8000/clients/1/update/
To add a project in client
POST: http://127.0.0.1:8000/clients/1/project/

To view all employees:
GET: http://127.0.0.1:8000/employees
To create a employee:
POST: http://127.0.0.1:8000/employees/create/
To update a employee
PUT: http://127.0.0.1:8000/employees/1/

To view all projects:
GET: http://127.0.0.1:8000/projects
To create a project:
POST: http://127.0.0.1:8000/projects/create/
To update a project
PUT: http://127.0.0.1:8000/projects/1/update/
To add an employee to a project
POST: http://127.0.0.1:8000/projects/1/employee/
