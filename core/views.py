# core/views.py

# django modules
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth  
from django.contrib import messages
from django.http import HttpResponse

# locals
from core.models import Profile

# Create your views here.

def index(request):
	return render(request, 'book/index.html')


def signup(request):

	# If the request method was POST or if the form was submitted
	if request.method == 'POST':
		# Get all data from form fields
		username 	= request.POST['username']
		email 		= request.POST['email']
		password 	= request.POST['password']
		password2 	= request.POST['password2']

		# Check if password == password2
		if password == password2:
			# Check if the email exist in the db
			if User.objects.filter(email=email).exists():
				# Send message
				messages.info(request, 'Email taken! Use another.')
				return redirect('signup')
			# Check if User exist in the db
			elif User.objects.filter(username=username).exists():
				# Send message
				messages.info(request, 'Username taken! Use another.')
				return redirect('signup')
			# Check if password == password2 and the username as well as
			# the email do not exist
			else:
				user = User.objects.create_user(
								username=username, 
								email=email, 
								password=password)
				user.save()

				# Log user in and redirect to settings page

				# Create a Profile object for the new user
				user_model = User.objects.get(username=username)
				new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
				new_profile.save()
				return redirect('signup')

		else:
			messages.info(request, 'Password not matching!')
			return redirect('signup')

	# If there is no request or if the form was not submitted
	else:	
	
		return render(request, 'book/signup.html')


def signin(request):

	# If sign in form was submitted
	if request.method == 'POST':
		# Check username and password
		username = request.POST['username'] 
		password = request.POST['password']

		# Authenticate username and password
		user = auth.authenticate(username=username, password=password)

		# If user exits in the db
		if user is not None: 
			# Let user login
			auth.login(request, user)
			# After user logged in, redirect user to the homepage
			return redirect('/') 

		# If user not exists or credentials not valid
		else:
			# Send user a message and redirect him/her to sign in page
			messages.info(request, 'In valid credentials!') 
			return redirect('signin')
	
	else:
		return render(request, 'book/signin.html')

