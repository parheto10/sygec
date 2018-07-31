from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from parametres import *
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'agec.views.home', name='home'),
    # url(r'^agec/', include('agec.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^pdf/', include('parametres.urls')),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
