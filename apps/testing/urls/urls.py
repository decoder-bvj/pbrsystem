from django.urls import path, include
from apps.testing.views import landing_view

urlpatterns = [
    # This includes all URLs from your core app
    path('', landing_view.landing , name="landing"),
]