# PR Test

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)

## Basic Commands

### Docker

With the assumption that Docker is installed and running, build the project for running locally using:

```bash
docker-compose -f local.yml build
```

Then run the stack with:
```bash
docker-compose -f local.yml up
```

This will start the project with the usual Django, DRF endpoints available
```
http://localhost:8000/
http://localhost:8000/api
http://localhost:8000/admin
```

Commands can be run against the project using the django container, for example to create a superuser:
```bash
docker-compose -f local.yml run --rm django python manage.py createsuperuser
```

### Setting Up Your Users

-   To create a **normal user account**, just go to [Sign Up](http://localhost:8000/accounts/signup/) and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

#### Running tests with pytest

```bash
docker-compose -f local.yml run --rm django pytest
```
