from django.shortcuts import render, redirect
from datetime import date
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
import numpy as np
# from django.http import HttpResponse, HttpResponseRedirect
from .models import FormSubmission
# from .passwords import hash_pass, verify_pass
import pickle
import os

with open("heart/lgbmclf.pkl", 'rb') as file:
    classifier = pickle.load(file)

# Create your views here.
@csrf_exempt 
def index(request):
    return render(request, "index.html", {"name": "blacklytning"})

@csrf_exempt 
def register(request):
    if request.method == 'POST':
        form_data = request.POST
        # hashed_pass = hash_pass(form_data["password"])
        # Person.objects.create(email=form_data["email"], name=form_data["name"], passphrase=hashed_pass)
        user = User.objects.create_user(email = form_data["email"], username = form_data["name"], password = form_data["password"])
        user.save()
        return redirect("/heart/login")
    return render(request, "register.html")


# def login_page(request):    
#     error_message = None  
#     if request.method == 'POST':
#         login_data = request.POST
#         # stored_data = Person.objects.filter(email=login_data["email"]).first()
#         user = User.objects.filter(username = login_data['username']).first()
#         if user is not None:
#             user = authenticate(username = login_data["username"], password = login_data["password"])
#             if user is not None: 
#                 login(request, user)
#                 print("success")
#                 return redirect("/heart/dashboard")
#             else:
#                 error_message = "Invalid username or password."
#         else:
#             error_message = "Invalid username or password."
#     return render(request, "login.html", {"error_message": error_message})
@csrf_exempt 
def login_page(request):
    error_message = None
    
    if request.method == 'POST':
        login_data = request.POST
        username = login_data.get('username')
        password = login_data.get('password')
        
        # Check if username and password are provided
        if not username or not password:
            error_message = "Please provide both username and password."
        else:
            # Authenticate user
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                print("success")
                return redirect("/heart/dashboard")
            else:
                error_message = "Invalid username or password."
    
    return render(request, "login.html", {"error_message": error_message})
@csrf_exempt 
def logout_page(request):
    logout(request)
    return redirect("/heart/login")

@csrf_exempt 
@login_required
def predict(request):
    prediction_made = False
    if request.method == "POST":
        form_data= request.POST
        prediction_made = True
        form_data = dict(form_data)
        age = int(form_data['age'][0])
        if age < 25:
            age = 1
        elif age < 30:
            age = 2
        elif age < 35:
            age = 3
        elif age < 40:
            age = 4
        elif age < 45:
            age = 5
        elif age < 50:
            age = 6
        elif age < 55:
            age = 7
        elif age < 60:
            age = 8
        elif age < 65:
            age = 9
        elif age < 70:
            age = 10
        elif age < 75:
            age = 11
        elif age < 80:
            age = 12
        else:
            age = 13 
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
            age
        ]).reshape(-1, 12)
        prediction = classifier.predict_proba(predictors)[0][1]
        if prediction >= 0.75:
            condition = "High Risk"
        elif prediction <= 0.5:
            condition = "Great Heart Health"
        else:
            condition = "Moderate Risk"
        FormSubmission.objects.create(
            username = request.user,
            time = date.today().strftime('%d-%m-%Y'),
            condition = condition,
            prediction = prediction,
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
            age = age
        )
    if prediction_made:
        return render(request, "predict.html",
        { "prediction" : prediction,
          "prediction_made" : prediction_made,  
          "username" : request.user,
        })
    else:
        return render(request, "predict.html")

@csrf_exempt   
@login_required
def dashboard(request):
    tests = FormSubmission.objects.filter(username = request.user).values()
    if tests is None:
        return render(request, "dashboard.html", {'no_tests' : "You haven't taken any tests yet"})
    else:
        return render(request, "dashboard.html", {'tests' : tests})
