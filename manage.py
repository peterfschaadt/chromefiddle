#!/usr/bin/env python
import os
import sys
from chromefiddle.settings.local_settings import *


if __name__ == "__main__":

    # Print name of environment
    print '### manage.py - Using local environment settings: %s' % ENV_STATE

    if ENV_STATE == 'PROD':
        # sys.path.append('/home/django/web/chromefiddle/chromefiddle/settings')
        print '### Entering production...'
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chromefiddle.settings.prod_settings")
    if ENV_STATE == 'DEV':
        # sys.path.append('/Users/peter/code/python/django/chromefiddle/chromefiddle/settings/')
        print '### Entering development...'
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chromefiddle.settings.dev_settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
