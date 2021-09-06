# core/admin.py

# django modules
from django.contrib import admin

# locals
from core.models import Profile  

# Register your models here.
admin.site.register(Profile)