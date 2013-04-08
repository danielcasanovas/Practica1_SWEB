from django.conf.urls import patterns, include, url 
from django.conf import settings
from teacherAvaluation.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', mainpage, name='home'),
    #url(r'^practica1/', include('practica1.foo.urls')),

    # Teachers:
    url(r'^teachers/$', teacher, name='teachers'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # Login
    url(r'^login/$', 'django.contrib.auth.views.login'),
)
if settings.DEBUG and settings.STATIC_ROOT:
    urlpatterns += patterns('',
        (r'%s(?P<path>.*)$' % settings.STATIC_URL.lstrip('/'), 
            'django.views.static.serve',
            {'document_root' : settings.STATIC_ROOT }),)
