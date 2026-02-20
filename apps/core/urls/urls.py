<<<<<<< HEAD
from django.urls import path, include
from apps.core.views.index_view import index
from apps.core.views.baseCard_view import basecard

urlpatterns = [
    # This includes all URLs from your core app
    path('', index, name="index"),
    path('basecard/',basecard, name='basecard'),
=======
from django.urls import path
# Import the specific module where your 'base' function lives
from core.view import base_view 

urlpatterns = [
    # Reference the module (base_view) and the function (base)
    path('', base_view.base, name="index"),
>>>>>>> 29c3e84 (Initial clean production-ready commit)
]