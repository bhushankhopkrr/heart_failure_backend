from django.shortcuts import render
from django.http import HttpResponse
from .models import Person
# Create your views here.

def index(request):
    return render(request,"index.html", { "name": "blacklytning"})

def register(request):
    Person.objects.create(first_name='black', last_name='lytning')
    return render(request,"register.html")

def login(request):
    return render(request,"login.html")