# config/urls.py

# django modules
from django.contrib import admin
from django.urls import path, include

# urlspatterns
urlpatterns = [
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
]
