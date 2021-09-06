# core/views.py

# django modules
from django.shortcuts import render

# locals

# Create your views here.

def index(request):
	return render(request, 'book/index.html')


def signup(request):
	return render(request, 'book/signup.html')