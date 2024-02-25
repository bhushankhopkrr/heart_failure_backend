from django.shortcuts import render
import numpy as np
from django.http import HttpResponse, HttpResponseRedirect
from .models import Person, FormSubmission
from .passwords import hash_pass, verify_pass
import pickle

with open('lgbmclf.pkl', 'rb') as file:
    classifier = pickle.load(file)


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
        # predictors = FormSubmission.objects.create(
        #     age = predictors['age'],
        #     highBP = predictors['highBP'],
        #     highChol = predictors['highChol'],
        #     smoker = predictors['smoker'],
        #     stroke = predictors['stroke'],
        #     diabetic = predictors['diabetic'],
        #     diffWalk = predictors['diffWalk'],
        #     mentalHlth = predictors['mentalHlth'],
        #     genHlth = predictors['genHlth'],
        #     physHlth = predictors['physHlth'],
        #     regEx = predictors['regEx'],
        #     bmi = predictors['bmi'],
        # )
    if prediction_made:
        return render(request, "predict.html",
        { "prediction" : prediction,
          "prediction_made" : prediction_made,  
        })
    else:
        return render(request, "predict.html")
