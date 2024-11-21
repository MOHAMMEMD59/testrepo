# ~/projects/django-web-app/merchex/listings/views.py

from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse('<h1>Hello Django!</h1>')

def aboutus(request):
     return HttpResponse('<h1>ABOUT US DJANGO TEAM!</h1>')

def contactus(request):
     return HttpResponse('<h1>Contact us<h1>')