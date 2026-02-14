from django.urls import path
from apps.dashboard.views import rout_control_view

urlpatterns = [
    # This includes all URLs from your core app
    path('rout/',rout_control_view, name='rout'),
]