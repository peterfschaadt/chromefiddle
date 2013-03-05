import sys
try:
    from common_settings import *
    from local_settings import *
except ImportError:
    pass


### Settings for Development environment ###

# export DJANGO_SETTINGS_MODULE=chromefiddle.settings.dev_settings

__author__ = 'Peter Schaadt'

# Enable debug mode to turn on detailed error pages
DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Import database credentials and secret key from local_settings
# local_settings is not tracked by Git
try:
    DEV_DB
except NameError:
    # Raise error and exit
    print "FATAL ERROR: Looks like you're missing the local_settings.py file for development!"
    sys.exit()

DATABASES = DEV_DB
SECRET_KEY = DEV_SECRET_KEY

# Development apps
# INSTALLED_APPS += ('debug-toolbar,')

# Email settings for contact form
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'peter.schaadt@gmail.com'
EMAIL_HOST_PASSWORD = DEV_EMAIL_PASSWORD
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = '/Users/peter/code/python/django/chromefiddle/media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = '/Users/peter/code/python/django/chromefiddle/static/'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    '/Users/peter/code/python/django/chromefiddle/src/',
)

TEMPLATE_DIRS = (
# Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
# Always use forward slashes, even on Windows.
# Don't forget to use absolute paths, not relative paths.
    '/Users/peter/code/python/django/chromefiddle/flags/templates/',
)
