from django.shortcuts import render
from django.http import HttpResponse
from .models import Person
# Create your views here.
from .passwords import hash_pass


def index(request):
    return render(request, "index.html", {"name": "blacklytning"})


def register(request):
    if request.method == 'POST':
        form_data = request.POST
        passphrase_bytes = form_data["password"].encode("utf-8")
        hashed_password = hash_pass(passphrase_bytes)
        Person.objects.create(email=form_data["email"], name=form_data["name"], passphrase= hashed_password)

    return render(request, "register.html")


def login(request):
    return render(request, "login.html")
