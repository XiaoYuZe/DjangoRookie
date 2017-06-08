from django.conf.urls import *
from monolog.views import bookinfo,bookdetails,bookcatalog,booksubject,bookhome


urlpatterns=[url(r'^$',bookhome),
	url(r'^book$',bookdetails),
	url(r'^cata$',bookcatalog),
	url(r'^subject$',booksubject),
	]