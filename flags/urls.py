from django.conf.urls import patterns, include, url
from django.views.generic.simple import redirect_to
from django.core.urlresolvers import reverse

urlpatterns = patterns('',
    url(r'^$', 'flags.views.home'),
    url(r'^home', 'flags.views.home'),
    url(r'^about', 'flags.views.about'),
)
