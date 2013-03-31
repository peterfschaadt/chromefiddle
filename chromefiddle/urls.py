from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from flags import views
import settings

# Admin enabled
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'chromefiddle.views.home', name='home'),
    # url(r'^flags/', include('chromefiddle.flags.urls')),

    # Admin documentation enabled
    url(r'^admin-only/doc/', include('django.contrib.admindocs.urls')),
    # Admin section enabled
    url(r'^admin-only/', include(admin.site.urls)),

    # Include robots.txt for search engine crawlers
    url(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
    # Include humans.txt with site information
    url(r'^humans\.txt$', TemplateView.as_view(template_name='humans.txt', content_type='text/plain')),

    # App-specific URLs
    url(r'^$', 'flags.views.home'),
    url(r'^home', 'flags.views.home'),
    url(r'^flags/$', 'flags.views.flags'),
    url(r'^flags/(?P<flag_id>\d+)/$', 'flags.views.details', name='details'),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^mac', 'flags.views.mac'),
    url(r'^windows', 'flags.views.windows'),
    url(r'^linux', 'flags.views.linux'),
    url(r'^chrome-os', 'flags.views.chrome_os'),
    url(r'^android', 'flags.views.android'),
    url(r'^info', TemplateView.as_view(template_name='info.html')),
    url(r'^advanced', TemplateView.as_view(template_name='advanced.html')),
    url(r'^about', TemplateView.as_view(template_name='about.html')),
    url(r'^contact', 'flags.views.contact'),
    url(r'^thanks', 'flags.views.thanks'),
    url(r'^privacy', TemplateView.as_view(template_name='privacy.html')),
)
