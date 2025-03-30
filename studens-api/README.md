## Introduction

Small API using django and django rest framework, implementing a CRUD for Student Model

## Base requirements

* Python 3.13

## Run the project
For run the project I recommend create a new virtual env using pyenv, UV or poetry

After that you can install the dependencies using

```pip install requirements```

Run the migrations with

```python manage.py migrate```

This project is using SQL lite DB so no further config is needed

For run the project you can use 

```python manage.py runserver```

after that you can enter to (localhost)

http://127.0.0.1:8000/api/schema/swagger-ui/

And you should see swagger API documentation


## Run the tests

For test running you should run the command

```python manage.py test```
