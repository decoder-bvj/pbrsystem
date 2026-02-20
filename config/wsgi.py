"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

<<<<<<< HEAD
<<<<<<< HEAD
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    os.getenv("DJANGO_SETTINGS_MODULE", "config.settings.prod")
)


=======
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
>>>>>>> 8356694 (Setup Dockerized Django project and fixed template errors)
=======
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.dev")
>>>>>>> 29c3e84 (Initial clean production-ready commit)

application = get_wsgi_application()
