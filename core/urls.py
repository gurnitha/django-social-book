# core/urls.py

# django modules
from django.urls import path

# locals
from core.views import index, signup  

# urlspatterns
urlpatterns = [
    path('', index, name='index'),
    path('signup/', signup, name='signup'),
]
