# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Index Page 
def index(request):
    return render(request, 'index.html')

# Login Page 
def loginPage(request):
    return render(request, 'loginpage.html')

# Signup Page 
def signupPage(request):
    return render(request, 'signuppage.html')
