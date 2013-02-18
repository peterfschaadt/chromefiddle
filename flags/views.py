from django.http import HttpResponse
from django.shortcuts import render
# import httpagentparser

def home(request):
    # user_agent = request.META['HTTP USER AGENT']
    # Parse user agent string for OS, browser, and version
    # user_info = httpagentparser.detect(user_agent)
    return render(request, 'home.html', {})
