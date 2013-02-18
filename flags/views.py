from django.http import HttpResponse
from django.shortcuts import render
import httpagentparser
from django.utils.log import getLogger
logger = getLogger('app')

def home(request):
    # Pull user agent string from request
    user_agent = request.META['HTTP USER AGENT']
    logger.warning('User agent string: ' + user_agent)
    # Parse user agent string for OS, browser, and version
    user_info = httpagentparser.detect(user_agent)
    logger.warning('User info: ' + user_info)
    return render(request, 'home.html', {})
