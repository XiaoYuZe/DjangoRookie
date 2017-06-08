from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from monolog.models import Book,Catalog,Subject
import os
# Create your views here.

monolog_DIR = os.path.join('','monolog')

def bookhome(request):
	return render_to_response('monohome.html',{'monolog_DIR':monolog_DIR})

def bookinfo(request):
	return HttpResponse('Hello This Waa1')

def bookdetails(request):
	objs = Book.objects.all()
	return render_to_response('bookauc.html',{'objects':objs,'monolog_DIR':monolog_DIR})

def bookcatalog(request):
	return render_to_response('bookcata.html',{'monolog_DIR':monolog_DIR})

def booksubject(request):
	return render_to_response('booksubject.html',{'monolog_DIR':monolog_DIR})