# ~/projects/django-web-app/merchex/listings/views.py

from django.http import HttpResponse
from django.shortcuts import render

from listing.models import Band




def hello(request):
    bands = Band.objects.all()
    return render(request, 'listing/hello.html',
    {'first_band': bands[0]})


def aboutus(request):
     return HttpResponse('<h1>ABOUT US DJANGO TEAM!</h1>')

def contactus(request):
     return HttpResponse('<h1>Contact us<h1>')