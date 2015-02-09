#from .views import AuthComplete, LoginError
from django.contrib import admin
from django.conf.urls import patterns, include, url
from views import *
admin.autodiscover() 

urlpatterns = patterns('',
    # some other urls
)