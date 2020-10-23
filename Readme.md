# Submission from Balu M N (balumn@ieee.org)

## Stack
* Django
* Celery (django-celery-results)
* Redis (Broker for celery)
* Sqlite3 (Django Backend- ORM)

## Install dependancies
    sudo apt install redis-server
    pip3 install -r requirments.txt

Project Name: `djangoproject`

username: `user`

password: `PassW0rd`

## Running
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver 0:8000
    ### Run on new terminal
    celery -A djangoproject worker -l INFO


# API Usages

### API 1
    GET /api/zip-codes/ HTTP/1.1
    Host: localhost:8000

### API 2
    GET /api/data/<zip_code>/ HTTP/1.1
    Host: localhost:8000

### API 3
    PUT /api/data/ HTTP/1.1
    Host: localhost:8000
    Content-Type: application/json
    {
        "zip": <zip_code>,
        "population": <population>
    }
