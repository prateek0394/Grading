from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Grading.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$','finalauth.views.home',name='home'),
    url(r'^logout/','finalauth.views.logout1',name='logout'),
    url(r'^exit/','finalauth.views.exit',name='exit'),
        url(r'^uploadData/','finalauth.views.upload',name='upload'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^grade/',include('gradingApp.urls')),
    url(r'^appSetting/',include('appSetting.urls')),
    url(r'^new-error-url/','finalauth.views.logout1',name='error'),
    url('', include('social_auth.urls'),name='social'),
    url('', include('django.contrib.auth.urls', namespace='auth')),

)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)