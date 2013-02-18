from django.http import HttpResponse
from django.shortcuts import render
import httpagentparser
from django.utils.log import getLogger
logger = getLogger('app')


def home(request):
    # Pull user agent string from web request
    user_agent = request.META['HTTP_USER_AGENT']
    logger.info('USER AGENT STRING: %s' % user_agent)
    # Parse user agent string for OS, browser, and version
    user_info = httpagentparser.detect(user_agent)
    logger.info('USER INFO: %s' % user_info)
    return render(request, 'home.html', {})
