## DJANGO BLOG
A small blog to practice setting up and running a django project from scratch.


### HOW TO RUN APPLICATION LOCALLY

- docker
```
cd docker
docker-compose up -d --build
# see blog app up running on localhost:8000
docker-compose down --remove-orphans # to stop running container
```

- cli
  - create virtual environment
  - pip install -r requirements.txt
  - pip install -r requirements_dev.txt
`python manage.py runserver`

### CLEAN CODE
Black for formatting and ruff for linting.

https://beta.ruff.rs/docs/

install requirements_dev.txt

- `ruff check .` -> ruff is used for linting
- `black .` -> black is used for formatting
- `mypy` -> mypy is used for typing


### HOW TO RUN MIGRATION

* `python manage.py makemigrations blog` -> creates migration file
* `python manage.py sqlmigrate blog 0001` -> outputs sql query without executing it
* `python manage.py migrate` -> applies migration
