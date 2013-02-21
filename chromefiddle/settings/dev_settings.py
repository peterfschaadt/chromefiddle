try:
    from common_settings import *
except ImportError:
    pass


### Settings for Development environment ###

__author__ = 'Peter Schaadt'

# Enable debug mode to turn on detailed error pages
DEBUG = True

# SQLite3 development database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '/Users/peter/Dropbox/Dev/Databases/chromefiddle-dev.db',  # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Development apps
# INSTALLED_APPS += ('debug-toolbar,')

# Static file directories
