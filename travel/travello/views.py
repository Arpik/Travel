from django.shortcuts import render
from .models import Destination
# Create your views here.

def index(request):

    dest1 = Destination()
    dest1.name = "Paris"
    dest1.desc = "The most romantic city"
    dest1.price = 800

    dest2 = Destination()
    
    
    return render(request, "index.html", {'dest1' : dest1})

def about(request):
    return render(request, "about.html")