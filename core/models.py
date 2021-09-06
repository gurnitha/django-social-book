# core/models.py

# django modules
from django.db import models
from django.contrib.auth import get_user_model

# locals

# Create your models here.

# Define User
User = get_user_model()

# CLASS:Profile
class Profile(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE) 
	id_user = models.ImageField() 
	bio = models.TextField(blank=True) 
	profileimg = models.ImageField(
			upload_to='profile/images', default='blank-profile-picture.png')
	location = models.CharField(max_length=100, blank=True)


	def __str__(self):
		return self.user.username