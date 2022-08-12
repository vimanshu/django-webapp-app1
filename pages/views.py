# this is where we handle request and response logic for the webapp
# what content is displayed on a given page

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def homePageView(request):
    return HttpResponse('Hello World!')
