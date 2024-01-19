from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Person, FormSubmission
from .passwords import hash_pass, verify_pass


# Create your views here.


def index(request):
    return render(request, "index.html", {"name": "blacklytning"})


def register(request):
    if request.method == 'POST':
        form_data = request.POST
        hashed_pass = hash_pass(form_data["password"])
        Person.objects.create(email=form_data["email"], name=form_data["name"], passphrase=hashed_pass)

    return render(request, "register.html")


def login(request):
    if request.method == 'POST':
        login_data = request.POST
        stored_data = Person.objects.filter(email=login_data["email"]).first()

        if verify_pass(stored_data.passphrase, login_data["password"]):
            print("SUCESSSSSSSSSS")

    return render(request, "login.html")


def predict(request):
    if request.method == "POST":
        predictors = request.POST
        print(predictors["BMI"])
    return render(request, "predict.html")

def checkPredictions(request):
    if request.metho == "POST":
        predictors = request.POST
        return HttpResponseRedirect(predictors["DiffWalk"])