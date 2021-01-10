## Setup

Setup virtual environment:

- Install pipenv

Install dependencies

```
pipenv shell
pipenv install -r requirements.txt
```

## Commands

- Run server

```
python manage.py runserver
```

- Make database migrations

```
python manage.py makemigrations
```

- Migrate database

```
python manage.py migrate
```

- Add new django app

```
python manage.py startapp <app_name>
```

## Admin Site Credentials

username: admin
password: nusfintechsoc

## Adding a Project with the Admin Dashboard

Projects for specific departments can be added with the admin dashboard.

1. Details can be added under the Project component
2. Images for the specific project can then be added from the Project Image section.

-Having multiple images is also suported. If multiple images are uploaded, a Carousel of the uploaded images will be shown.
-If no images are uploaded for the specific project, a default image will be shown (coded on the frontend).
