<<<<<<< HEAD
from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_default_auto_field = 'django.db.models.BigAutoField'
    name = "apps.core"
=======
# apps/core/apps.py

from django.apps import AppConfig

class CoreConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    # This MUST match the path in INSTALLED_APPS
    name = "apps.core"
>>>>>>> 29c3e84 (Initial clean production-ready commit)
