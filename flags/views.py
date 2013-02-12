from django.http import HttpResponse

def home(request):
    return HttpResponse('This is the Google Chrome experimental flag index from chrome://flags')
