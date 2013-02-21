try:
    from common_settings import *
except ImportError:
    pass


### Settings for Production environment ###

__author__ = 'Peter Schaadt'

# Disable debug mode to turn off detailed error pages
DEBUG = False

DATABASES = {
    # PostgreSQL production database
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'chromefiddle-prod',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Production apps
# INSTALLED_APPS += (',')

# Static file directories
