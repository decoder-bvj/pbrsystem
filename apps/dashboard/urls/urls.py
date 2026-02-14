from django.urls import path, include
from apps.dashboard import views

urlpatterns = [
    # This includes all URLs from your core app
    path('basecard/',views.dashboard, name='basecard'),
    path('',views.dashboard,name='dashboard'),
    path('rout/',include('rout_urls')),
]