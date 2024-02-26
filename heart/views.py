from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import numpy as np
# from django.http import HttpResponse, HttpResponseRedirect
from .models import Person, FormSubmission
# from .passwords import hash_pass, verify_pass
import pickle

with open('lgbmclf.pkl', 'rb') as file:
    classifier = pickle.load(file)

# Create your views here.
def index(request):
    return render(request, "index.html", {"name": "blacklytning"})


def register(request):
    if request.method == 'POST':
        form_data = request.POST
        # hashed_pass = hash_pass(form_data["password"])
        # Person.objects.create(email=form_data["email"], name=form_data["name"], passphrase=hashed_pass)
        user = User.objects.create_user(email = form_data["email"], username = form_data["name"], password = form_data["password"])
        user.save()
        return redirect("/heart/login")
    return render(request, "register.html")


def login_page(request):
    if request.method == 'POST':
        login_data = request.POST
        # stored_data = Person.objects.filter(email=login_data["email"]).first()
        user = User.objects.filter(username = login_data['username']).first()
        print(type(login_data['username']))
        if user is not None:
            user = authenticate(username = login_data["username"], password = login_data["password"])
            if user is not None: 
                login(request, user)
                print("success")
                return redirect("/heart/dashboard")
    return render(request, "login.html")

def logout_page(request):
    logout(request)
    return redirect("/heart/login")

@login_required
def predict(request):
    prediction_made = False
    if request.method == "POST":
        form_data= request.POST
        prediction_made = True
        form_data = dict(form_data)
        predictors = np.array([
            int(form_data['highBP'][0]),
            int(form_data['highChol'][0]),
            int(form_data['bmi'][0]),
            int(form_data['smoker'][0]),
            int(form_data['stroke'][0]),
            int(form_data['diabetic'][0]),
            int(form_data['regEx'][0]),
            int(form_data['genHlth'][0]),
            int(form_data['mentalHlth'][0]),
            int(form_data['physHlth'][0]),
            int(form_data['diffWalk'][0]),
            int(form_data['age'][0]),
        ]).reshape(-1, 12)
        prediction = classifier.predict_proba(predictors)[0][1]
        if prediction >= 0.75:
            condition = "High Risk"
        elif prediction <= 0.5:
            condition = "Great Heart Health"
        else:
            condition = "Moderate Risk"
        FormSubmission.objects.create(
            highBP = int(form_data['highBP'][0]),
            highChol = int(form_data['highChol'][0]),
            bmi = int(form_data['bmi'][0]),
            smoker = int(form_data['smoker'][0]),
            stroke = int(form_data['stroke'][0]),
            diabetic = int(form_data['diabetic'][0]),
            regEx = int(form_data['regEx'][0]),
            genHlth = int(form_data['genHlth'][0]),
            mentalHlth = int(form_data['mentalHlth'][0]),
            physHlth = int(form_data['physHlth'][0]),
            diffWalk = int(form_data['diffWalk'][0]),
            age = int(form_data['age'][0]),
            prediction = prediction,
            condition = condition,
        )
    if prediction_made:
        return render(request, "predict.html",
        { "prediction" : prediction,
          "prediction_made" : prediction_made,  
          "username" : request.user,
        })
    else:
        return render(request, "predict.html")
    
@login_required
def dashboard(request):
    return render(request, "dashboard.html")