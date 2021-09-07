# core/urls.py

# django modules
from django.urls import path

# locals
from core.views import index, signup, signin  

# urlspatterns
urlpatterns = [
    path('', index, name='index'),
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
]
