from django.conf.urls import *
# from django.conf.urls import patterns
from highone.views import index,baseone,zao3,indexb,homen,pagepa,wegetcha,login_in,login,regist

# urlpatterns = patterns('',url(r'^$',login),
# 	url(r'^one$',baseone),
# 	url(r'^two$',zao3),
# 	url(r'^thd$',indexb),
# 	url(r'^fth$',pagepa),
# 	url(r'^fita$',wegetcha),
# 	url(r'^login$',login), 
# 	url(r'^regist$',regist),
# 	url(r'^index$',baseone),
# 	)

urlpatterns = [url(r'^$',login),
	url(r'^one$',baseone),
	url(r'^two$',zao3),
	url(r'^thd$',indexb),
	url(r'^fth$',pagepa),
	url(r'^fita$',wegetcha),
	url(r'^login$',login), 
	url(r'^regist$',regist),
	url(r'^index$',baseone),
	]