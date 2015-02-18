from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sequencerapi.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^illuminaapi/', include('apps.illuminaapi.urls')),
)
