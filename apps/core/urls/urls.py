from django.urls import path, include
from apps.core.views.index_view import index
from apps.core.views.baseCard_view import basecard

urlpatterns = [
    # This includes all URLs from your core app
    path('', index, name="index"),
    path('basecard/',basecard, name='basecard'),
]