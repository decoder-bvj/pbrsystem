<<<<<<< HEAD
from .base import *

DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

<<<<<<< HEAD
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "static"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
=======
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DEV_DB_NAME"),
        "USER": os.getenv("DEV_DB_USER"),
        "PASSWORD": os.getenv("DEV_DB_PASSWORD"),
        "HOST": os.getenv("DEV_DB_HOST"),
        "PORT": "5432",
>>>>>>> 8356694 (Setup Dockerized Django project and fixed template errors)
    }
}
=======
# config/settings/dev.py
from .base import *

# This tells Django to use the DATABASE_URL we just fixed in .env.dev
DATABASES = {
    'default': env.db()
}

DEBUG = True
>>>>>>> 29c3e84 (Initial clean production-ready commit)
