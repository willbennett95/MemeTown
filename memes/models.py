# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

# Users
class User(models.Model):
	email = models.CharField(max_length=255, primary_key=True)
	password = models.CharField(max_length=255, default='password')
