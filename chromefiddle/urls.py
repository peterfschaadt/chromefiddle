from django.conf.urls import patterns, include, url

# Admin enabled
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'chromefiddle.views.home', name='home'),
    # url(r'^chromefiddle/', include('chromefiddle.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Admin enabled
    url(r'^admin/', include(admin.site.urls)),
)
