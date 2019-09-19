from django.shortcuts import render
from .models import Destination
# Create your views here.

def index(request):

    dest1 = Destination()
    dest1.name = "Paris"
    dest1.desc = "The most romantic city"
    dest1.price = 800

    dest2 = Destination()
    dest2.name = "London"
    dest2.desc = "The City of lights"
    dest2.price = 900
    
    dest3 = Destination()
    dest3.name = "Milan"
    dest3.desc = "The City of lights"
    dest3.price = 900
    
    dest4 = Destination()
    dest4.name = "Rome"
    dest4.desc = "The City of history"
    dest4.price = 600

    
    dest5 = Destination()
    dest5.name = "Amsterdam "
    dest5.desc = "The city of bikes"
    dest5.price = 500

    
    dest6 = Destination()
    dest6.name = "Bacabal"
    dest6.desc = "The city of love..."
    dest6.price = 1900

    dests = [dest1, dest2, dest3, dest4, dest5, dest6] 

    return render(request, "index.html", {'dests' : dests})

def about(request):
    return render(request, "about.html")