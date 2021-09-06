# core/urls.py

# django modules
from django.urls import path

# locals
from core.views import index  

# urlspatterns
urlpatterns = [
    path('', index, name='index'),
]
