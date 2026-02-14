from .base import *
<<<<<<< HEAD
import os

DEBUG = False

ALLOWED_HOSTS = ["yourdomain.com", "www.yourdomain.com"]
=======

DEBUG = False

ALLOWED_HOSTS = ["your-ec2-public-ip"]
>>>>>>> 8356694 (Setup Dockerized Django project and fixed template errors)

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
<<<<<<< HEAD
        "NAME": os.getenv("POSTGRES_DB"),
        "USER": os.getenv("POSTGRES_USER"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD"),
        "HOST": os.getenv("POSTGRES_HOST", "db"),
        "PORT": 5432,
    }
}

SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
=======
        "NAME": os.getenv("PROD_DB_NAME"),
        "USER": os.getenv("PROD_DB_USER"),
        "PASSWORD": os.getenv("PROD_DB_PASSWORD"),
        "HOST": os.getenv("PROD_DB_HOST"),
        "PORT": "5432",
    }
}

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
>>>>>>> 8356694 (Setup Dockerized Django project and fixed template errors)
