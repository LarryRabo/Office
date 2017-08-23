from django.conf.urls import url
from login import views

urlpatterns=[
    url(r'^$', views.login, name='login'),
    url(r'^login/$', views.login, name='login'),
    url(r'^regist/$', views.regist, name='regist'),
    url(r'^index/$', views.index, name='index'),
    url(r'^logout/$', views.logout, name='logout'),

]


#http://www.cnblogs.com/fnng/p/3750596.html