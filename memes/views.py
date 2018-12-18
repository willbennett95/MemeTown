# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#from django.shortcuts import render
#from django.http import HttpResponse

from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
from django.http import HttpResponse, JsonResponse, Http404
from .models import User
import hashlib

def loggedin(f):
    def test(request):
        if 'email' in request.session:
            return f(request)
        else:
            return render(request, 'base.html')
return test

# Index Page 
def index(request):
    return render(request, 'index.html')
@loggedin
def userindex(request):
	e = request.session['email']
	return render(request, 'index.html', {'email':e, 'loggedin': True})

# Hash password
def hash_password(password):
	# Salting the password to make it harder to decode
    s1 = 'hqb%$t'
    s2 = 'cg*l'
    # Using sha256 to encrypt the password with added salt
    return hashlib.sha256(s1.encode() + password.encode()).hexdigest() + ':' + s2

# Login 
def login(request):
	if 'email' not in request.POST: # If no email is found, go to login page
		return render(request, 'loginpage.html')
	else: # If user has entered an email, log them in
		e = request.POST['email'] # Get email from page
		p = request.POST['password'] #Get password from page
		try: # Check if email exists in database
			u = User.objects.get(pk=e)
			p = hash_password(p) # Encrypt password from input
			# Check if password from input and database match 
			if p == u.password:
				# Add email and name to session
				request.session['email'] = e;
				return render(request, 'index.html', {'email': e, 'loggedin': True})
			# If password doesn't match
			else:
				error = "Incorrect Username or Password" # Error message to be passed to login page
				return render(request, 'loginpage.html', {'error': error})
		except User.DoesNotExist: # If email doesn't exist in database 
			error = "Incorrect Username or Password" # Error message to be passed to login page
			return render(request, 'loginpage.html', {'error': error})

# Signup
def signup(request):
	print(request.body)
	if 'email' not in request.POST:
		return render(request, 'signuppage.html')
	else:
		e = request.POST['email']
		try:
			e = User.objects.get(pk=e)
			return render(request, 'signuppage.html')
		except User.DoesNotExist:
			p = request.POST['password'].strip()
			p = hash_password(p)
			e = request.POST['email'].strip()
			u = User(email=e, password=p)
			u.save()
			request.session['email'] = e;
			return render(request, 'index.html', {'email':e, 'loggedin': True})
