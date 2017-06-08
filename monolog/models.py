from __future__ import unicode_literals

from django.db import models
from django.contrib import admin

# Create your models here.

class Book(models.Model):
	title = models.CharField(max_length=50)
	author = models.CharField(max_length=20)
	press = models.CharField(max_length=30)
	price = models.CharField(max_length=20)


class Catalog(models.Model):
	title = models.CharField(max_length=50)
	catalog_code = models.CharField(max_length=30)  	# Books Catalog Code
	catalog_name = models.CharField(max_length=50)	# Books Catalog Name


class Subject(models.Model):
	title = models.CharField(max_length=50)
	subject_code = models.CharField(max_length=10)  	# Subjects code
	subject_name = models.CharField(max_length=30)	# Subjects name

admin.site.register(Book)
admin.site.register(Catalog)
admin.site.register(Subject)