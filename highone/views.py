from django.shortcuts import render
from highone.models import Wenting,Hobby
from django.template import Context,loader,RequestContext
from django.template.response import TemplateResponse
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger
import MySQLdb
from django.contrib.auth.decorators import login_required
from django import forms
from models import User
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
class UserForm(forms.Form):
	username = forms.CharField(label='usrn',max_length=100)
	password = forms.CharField(label='pswd',widget=forms.PasswordInput())

def index(request):
	w = Wenting.objects.all().values()
	t = loader.get_template('high.html')
	c = Context({'name':'23ff','jobs':'jobjj'})
	return render_to_response('high.html',{'name':w[2]['name'],'jobs':w[2]['jobs'],'age':w[2]['age']})

def baseone(request):
	h = Hobby.objects.all()
	t = loader.get_template('baseone.html')
	# print 'h',h
	return TemplateResponse(request,'baseone.html',{'objects':h})

def zao3(request):
	return render_to_response('zao3.html')

def indexb(request):
	w = Wenting.objects.all().values()
	t = loader.get_template('highb.html')
	c = Context({'name':'23ff','jobs':'jobjj'})
	return render_to_response('highb.html',{'name':w[2]['name'],'jobs':w[2]['jobs'],'age':w[2]['age']})

def homen(request):
	return render_to_response('home.html')

# @login_required
def pagepa(request):
	h = Hobby.objects.all()
	pag = Paginator(h,2)
	# print 'h',h
	page = request.GET.get('page')
	try:
		contains = pag.page(page)
	except PageNotAnInteger:
		contains = pag.page(1)
	except EmptyPage:
		contains = pag.page(pag.num_pages)
	return render_to_response('pagepa.html',{'objects':contains,'contains':contains})
	# return TemplateResponse(request,'pagepa.html',{'objects':contains})

# @login_required
def wegetcha(request):
	conn = MySQLdb.connect(host='172.16.0.20',port=3306,user='zhangxiaogang',passwd='gangxiaozhang',db='court_notice',charset='utf8')
	cursor=conn.cursor()	
	sql = 'select * from bjcourt limit 150'
	cursor.execute(sql)
	h = cursor.fetchall()

	pag = Paginator(h,5)
	# print 'h',h
	page = request.GET.get('page')
	try:
		contains = pag.page(page)
	except PageNotAnInteger:
		contains = pag.page(1)
	except EmptyPage:
		contains = pag.page(pag.num_pages)
	return render_to_response('datasehere.html',{'objects':contains,'contains':contains})
	# return TemplateResponse(request,'pagepa.html',{'objects':contains})	

def login_in(request):
	return render_to_response('login.html')

@csrf_exempt
def regist(request):
	if request.method == 'POST':
		uf = UserForm(request.POST)
		if uf.is_valid():
			print uf
			username = uf.cleaned_data['username']
			password = uf.cleaned_data['password']

			User.objects.create(username=username,password=password)
			return HttpResponse('regist success')
	else:
		uf = UserForm()
	# return render_to_response('regist.html',{'uf':uf},context_instance=RequestContext(request))
        return render_to_response('regist.html',{'uf':uf})

@csrf_exempt
def login(request):
	if request.method == 'POST':
		uf = UserForm(request.POST)
		if uf.is_valid:
			print 'login_uf',uf
			username = uf.cleaned_data['username']
			password = uf.cleaned_data['password']

			user = User.objects.filter(username__exact=username, password__exact=password)
			if user:
				response = HttpResponseRedirect('/index')
				response.set_cookie('username',username,3600)
				return response
			else:
				return HttpResponseRedirect('/regist')

	else:
		uf = UserForm()
	# return render_to_response('login.html',{'uf':uf},ontext_instance=RequestContext(request))
        return render_to_response('login.html',{'uf':uf})

def index_true(request):
	username = request.COOKIES.get('username','')
	return render_to_response('index.html',{'username':username})

def logout(request):
	response = HttpResponse('logout le')
	response.delete_cookie('username')
	return response

def login1(request):

	return render_to_response('login1.html')
