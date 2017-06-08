from __future__ import unicode_literals

from django.db import models
from django.contrib import admin
# Create your models here.
class Wenting(models.Model):
	name = models.CharField(max_length = 50)
	age = models.CharField(max_length = 5)
	jobs = models.CharField(max_length = 20)

class Hobby(models.Model):
	name = models.CharField(max_length = 50,default='***')	# name
	rank = models.CharField(max_length = 5,default='0')		# ranking
	modn = models.CharField(max_length = 20,default='act')	# type
	prof = models.CharField(max_length = 500,default='Dis')	# profile
	pric = models.CharField(max_length = 10,default='0')	# price

class User(models.Model):
	username = models.CharField(max_length=50)
	password = models.CharField(max_length=50)

admin.site.register(Wenting)
admin.site.register(Hobby)
admin.site.register(User)