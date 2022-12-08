# NVISH-python-exercise

## Purpose

The purpose of these exercises is to establish a common, non-biased
baseline for comparisons of developer skills and abillity using the
development language Python.

---

## Prerequisuites

[Python](https://www.python.org/downloads/)

[Docker (optional for redis)](https://docs.docker.com/engine/install/ubuntu/)

[Docker compope (optional for redis)](https://docs.docker.com/compose/install/linux/#install-the-plugin-manually)

---

## Setup

Clone the project:

```sh
git clone https://github.com/mr-engin3er/NVISH-python-exercise.git
```

Go to the project directory:

```sh
cd NVISH-python-exercise
```

Create virtual environment using venv:

```sh
python -m venv env
```

Activate virtual environment:

```sh
source ./env/bin/activate
```

Install requirements using pip:

```sh
pip install -r requirements.txt
```

Rename .env and set environment variables:

```sh
mv env.example .env
```

Create DB , Tables and admin user:

```sh
python init_db.py
```

Setup redis in local using docker (optional):

```sh
docker compose up -d
```

Run server:

```sh
python main.py
```

---

## Project Structure

    ├── docker-compose.yaml
    ├── init_db.py
    ├── main.py
    ├── NVISH_exercise_dev.db
    ├── README.md
    ├── src
    │   ├── app.py
    │   ├── config.py
    │   ├── exercise1.py
    │   ├── exercise2.py
    │   ├── exercise3.py
    │   ├── __init__.py
    │   ├── redis_utils.py
    │   └── utils.py
    └── test
        ├── conftest.py
        ├── __init__.py
        ├── test_app.py
        ├── test_exercise1.py
        ├── test_exercise2.py
        ├── test_exercise3.py
        ├── test_redis_utils.py
        └── test_utils.py

---

## API tesing using CURL

- `/ping`

```curl
curl --location --request GET '127.0.0.1:5000/ping' \
--data-raw ''
```

- `/login`

```curl
curl --location --request POST '127.0.0.1:5000/login' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username":"admin",
    "password":"Admin@123"
}'
```

- `/authorize`

```curl
curl --location --request GET '127.0.0.1:5000/authorize' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwidXNlcm5hbWUiOiJhZG1pbiIsInBhc3N3b3JkIjoicGJrZGYyOnNoYTI1NjoyNjAwMDAkbWttRDFrN0hqSXRKelVSVyRjZWJlMTQwNDUwNmE1NzQ1OGZkODcwNWFlYTM4M2YxOGVkOTZhNTc0NmMyZjZmZDZjMWU4NWQwZjA3OWVhNzY3In0.OkehVsrcmNF1ME_i8Zr-4AIwdohY-7pYZywXf1EsDQs' \
--data-raw ''
```

- `/save`

```curl
curl --location --request POST '127.0.0.1:5000/save' \
--header 'Content-Type: application/json' \
--data-raw '{
    "title" : "first post",
    "content": "Big content of first post"
}'
```

- `/get`

```curl
curl --location --request GET '127.0.0.1:5000/get' \
--data-raw ''
```

- `/get/<post_id>`

```curl
curl --location --request GET '127.0.0.1:5000/get/1' \
--data-raw ''
```

- `/delete`

```curl
curl --location --request DELETE '127.0.0.1:5000/delete' \
--data-raw ''
```

- `/delete/<post_id>`

```curl
curl --location --request DELETE '127.0.0.1:5000/delete/11' \
--data-raw ''
```

---

Run unit testcases using PyTest (Linux):

```sh
export ENV=test && pytest --cov=src test/
```

Run unit testcases using PyTest (Windows):

```sh
set ENV=test && pytest --cov=src test/
```

### Note:- ` Please kill your terminal after running testcases because it'll set your ENV to test. Which will cause issues in development or production environment`

---
