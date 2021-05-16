# NUS FinTech Website Backend

This repository contains the code for the backend of the official NUS FinTech Website.

It is a django project using the django rest framework and is deployed on the google app engine with mySQL as the database in cloud SQL.

## Installation

1. Clone repository.

2. Set up virtual environment:

  - Install [pipenv](https://docs.python-guide.org/dev/virtualenvs/)

  - Install dependencies
```
pipenv shell
pipenv install -r requirements.txt
```

3. Obtain env file with the credentials for settings.py and place the env file in the root directory.

## Getting Started

### Running local server with connection to production database

1. Ensure settings.py is correct, the following lines **SHOULD** be commented in site_drf/settings.py.
```
# [RUNNING LOCALLY AND USING IN-MEMORY SQLITE3 DATABASE INSTEAD OF PRODUCTION CLOUDSQL DATABASE]
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
#     }
# }
```

2. Start Cloud SQL Proxy on a separate terminal: ./cloud_sql_proxy -instances="[YOUR_INSTANCE_CONNECTION_NAME]"=tcp:[PORT_NUMBER]
```
./cloud_sql_proxy -instances="data-eye-289210:asia-southeast1:fintech-website-instance"=tcp:3307
```

3. Run server
```
pipenv shell
python manage.py runserver
```

### Running local server with connection to local sqlite testing database
1. Ensure settings.py is correct, the following lines **SHOULD NOT** be commented in site_drf/settings.py.
```
# [RUNNING LOCALLY AND USING IN-MEMORY SQLITE3 DATABASE INSTEAD OF PRODUCTION CLOUDSQL DATABASE]
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
    }
}
```

2. Run server
```
pipenv shell
python manage.py runserver
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

## Deployment

### Intro
The app is deployed on the GCP platform through the google app engine. The url of the app is https://data-eye-289210.df.r.appspot.com/

### Redeploying

1. Login to an authorised gcloud account
```
gcloud auth application-default login
```

2. Navigate to project directory, create isolated Python environment and install dependencies
```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

3. Run Django migrations 
```
python manage.py makemigrations
python manage.py migrate
```

4. Deploy
```
python manage.py collectstatic
gcloud app deploy
```

* More details can be found in the youtube tutorial and official docs under reference links. One difference is that we are following the youtube tutorial for step 1 instead for following the official docs because we are using 
python 3.

### Reference Links for deployment

- https://www.youtube.com/watch?v=8Vxo0P_P8TU&ab_channel=BenjaminCarlson
- https://cloud.google.com/python/django/appengine


## Image Hosting

Any method that is able to provide an image URL can be used. For now, all of the images are posted on [imgur](https://imgur.com/) and the image URL is obtained by getting the BBCode which is then stored in the database.

## Adding a Project with the Admin Dashboard

Projects for specific departments can be added with the admin dashboard. Credentials can be obtained from exco members.

1. Details can be added under the Project component
2. Images for the specific project can then be added from the Project Image section.

- Having multiple images is also suported. If multiple images are uploaded, a Carousel of the uploaded images will be shown.
- If no images are uploaded for the specific project, a default image will be shown (coded on the frontend).
