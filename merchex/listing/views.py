# ~/projects/django-web-app/merchex/listings/views.py

from django.http import HttpResponse
from django.shortcuts import render

from listing.models import Band

def hello(request):
    bands = Band.objects.all()
    return HttpResponse(f"""
        <h1>Hello Django !</h1>
        <p>Mes groupes préférés sont :<p>
        <ul>
            <li>{bands[0].name}</li><li>{bands[3].title}</li>
            <li>{bands[1].name}</li><li>{bands[4].title}</li>
            <li>{bands[2].name}</li> <li>{bands[5].title}</li>
        </ul>
      
""")


def aboutus(request):
     return HttpResponse('<h1>ABOUT US DJANGO TEAM!</h1>')

def contactus(request):
     return HttpResponse('<h1>Contact us<h1>')