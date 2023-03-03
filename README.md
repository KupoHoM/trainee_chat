# Trainee project "Simple Chat"
## Project description

The "Simple Chat" project is an API developed using Python/Django/DRF, with endpoints configured for easy registration and URLs for JWT token usage. The "api/" section has a convenient use of ModelViewSet in applications.

## Tech stack
[![Pyhton](https://img.shields.io/badge/python-%23000.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/-DRF-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.django-rest-framework.org/)





## Installation

Before you start, make sure you have [Python](https://www.python.org/downloads/release/python-3110/) v3.11+ and pip installed. 


Create a virtual environment
```
python -m venv venv
```
Activate the virtual environment

```
Windows:
    .\venv\Scripts\activate
Unix or Linux:
    source venv/bin/activate
```
Clone a repository from GitHub
```
git clone https://github.com/KupoHoM/trainee_chat.git
```
Install the dependencies

```sh
pip install -r requirements.txt
```
Configure the database
```sh
python manage.py makemigrations
python manage.py migrate
```
Сreate superuser
```
python manage.py createsuperuser
```
Start server
```
python manage.py runserver
```
## Project Structure
If you have successfully launched a project, you will start developing it. 
Project files are located in project folders.

- The settings.py file contains project settings, such as the database, paths to static files, project language, etc.
- The urls.py file contains the addresses of the project pages.
- The views.py file contains the project logic.
- The models.py file contains the database models.
- The admin.py allows you to register models that will be available in the admin interface. 
- The serializers.py contains code for serializing and deserializing complex data types, such as models.
- The simple_chat folder with basic project settings
