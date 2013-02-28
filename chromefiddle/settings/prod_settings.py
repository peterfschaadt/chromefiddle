import sys
try:
    from common_settings import *
    from local_settings import *
except ImportError:
    pass


### Settings for Production environment ###

# export DJANGO_SETTINGS_MODULE=chromefiddle.settings.prod_settings

__author__ = 'Peter Schaadt'

# Disable debug mode to turn off detailed error pages
DEBUG = False
TEMPLATE_DEBUG = DEBUG

# Import database credentials and secret key from local_settings
# local_settings is not tracked by Git
try:
    PROD_DB
except NameError:
    # Raise error and exit
    print "FATAL ERROR: Looks like you're missing the local_settings.py file for production!"
    sys.exit()

DATABASES = PROD_DB
SECRET_KEY = PROD_SECRET_KEY

# Production apps
# INSTALLED_APPS += (',')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = '/home/django/web/chromefiddle/static/'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    '/home/django/web/chromefiddle/src/',
)

TEMPLATE_DIRS = (
# Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
# Always use forward slashes, even on Windows.
# Don't forget to use absolute paths, not relative paths.
    '/home/django/web/chromefiddle/flags/templates/',
)
