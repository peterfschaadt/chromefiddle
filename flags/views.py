from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.simple import direct_to_template
import httpagentparser
from flags.models import Flag
from django.utils.log import getLogger
logger = getLogger('app')


def home(request):
    """
    View for Home page.
    """
    # Pull user agent string from web request
    user_agent = request.META['HTTP_USER_AGENT']
    logger.info('USER AGENT STRING: %s' % user_agent)
    # Parse user agent string for OS, browser, and version
    user_info = httpagentparser.detect(user_agent)
    logger.info('USER INFO: %s' % user_info)
    # test_user_info = {'flavor': {'version': 'X 10.8.2', 'name': 'MacOS'}, 'os': {'name': 'Macintosh'}, 'browser': {'version': '24.0.1312.57', 'name': 'Chrome'}}

    # Check for operating system type
    operating_system = user_info['os']['name'].lower()
    if operating_system == 'macintosh':
        os = 'Mac OS X'
    elif operating_system == 'windows':
        os = 'Windows'
    elif operating_system == 'linux':
        os = 'Linux'
    elif operating_system == 'chrome-os':
        os = 'Chrome OS'
    elif operating_system == 'android':
        os = 'Android'
    else:
        os = 'an unfamiliar OS'

    return render(request, 'home.html', {'os': os, 'browser': user_info['browser']})


def list(request):
    """
    View for page listing all flags.
    """
    all_flags = Flag.objects.all()
    flag_count = all_flags.count()
    logger.info('TOTAL FLAGS: %d' % flag_count)
    return render(request, 'list.html', {'flag_count': 'flag_count'})


def about(request):
    """
    View for About page.
    """
    # return render(request, 'about.html', {})
    return direct_to_template(request, 'about.html', {})


def privacy(request):
    """
    View for Privacy page.
    """
    return render(request, 'privacy.html', {})
