from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import *
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Grading.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$',index),
    url(r'^dissertation$',dissertation),
 	url(r'^RP$',researchPractice),
 	url(r'^student$',student),
 	url(r'^reportDisp$',reportDisp),
 	url(r'^submitReport$',reportSubmit),
 	url(r'^courses$',courses),
    url(r'^thesis$',thesis),
    url(r'^projects$',projects),
    url(r'^reportGen$',reportGen),
    url(r'^reminder$',reminder),
    url(r'^marks$',marks),
)
