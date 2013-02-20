from django.conf.urls import patterns, include, url
from django.views.generic.simple import redirect_to
from flags import views
import settings

# Admin enabled
from django.contrib import admin
admin.autodiscover()

# Import URLs from apps
import flags.urls


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'chromefiddle.views.home', name='home'),
    # url(r'^chromefiddle/', include('chromefiddle.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # App-specific URLs
    # url(r'^$', 'flags.views.home'),
    url(r'^$', include(flags.urls)),
    # Original:
    # url(r'^flags/', include(flags.urls)),

    # Admin enabled
    url(r'^admin/', include(admin.site.urls)),

    # url(r'.*', redirect_to, {'url': '/flags/home'}),
)
