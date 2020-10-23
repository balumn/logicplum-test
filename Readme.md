# Submission from Balu M N (balumn@ieee.org)

## Stack
* Django
* Celery (django-celery-results)
* Redis (Broker for celery)
* Sqlite3 (Django Backend- ORM)

## Install dependancies
    sudo apt install redis-server
    pip3 install -r requirments.txt

## installation
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver 0:8000
    ### Run on new terminal
    celery -A djangoproject worker -l INFO

Login Page : `host_ip:8000/admin/`

username: `user`

password: `PassW0rd`

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

Example

    curl --location --request PUT 'http://localhost:8000/api/data/' \
    --header 'Content-Type: application/json' \
    --data-raw '    {
            "zip": 603,
            "population": 48816
        }'

### API 4
    POST /api/data/ HTTP/1.1
    Host: localhost:8000
    Content-Type: application/json

    {
        "zip": <int>,
        "lat": <float>,
        "lng": <float>,
        "city": <string>,
        "state_id": <string>,
        "state_name": <string>,
        "zcta": <bool>,
        "parent_zcta": null,
        "population": <int>,
        "density": <float>,
        "county_fips": <int>,
        "county_name": <string>,
        "county_weights": <json_string>,
        "county_names_all": <string>,
        "county_fips_all": <string>,
        "imprecise": <bool>,
        "military": <bool>,
        "timezone": <string>
    }

Example

    curl --location --request POST 'http://localhost:8000/api/data/' \
    --header 'Content-Type: application/json' \
    --data-raw '{
        "zip": 1,
        "lat": 18.45439,
        "lng": -67.12202,
        "city": "Aguadilla",
        "state_id": "PR",
        "state_name": "Puerto Rico",
        "zcta": true,
        "parent_zcta": null,
        "population": 48814,
        "density": 667.9,
        "county_fips": 72005,
        "county_name": "Aguadilla",
        "county_weights": {
            "72005": 100
        },
        "county_names_all": "Aguadilla",
        "county_fips_all": "72005",
        "imprecise": false,
        "military": false,
        "timezone": "America/Puerto_Rico"
    }'