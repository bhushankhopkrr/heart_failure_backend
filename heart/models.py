from django.db import models


# Create your models here.
class Person(models.Model):
    email = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    passphrase = models.CharField(max_length=500)

class FormSubmission(models.Model):
    age = models.IntegerField()
    sex = models.CharField()
    highBP = models.CharField()
    highChol = models.CharField()
    smoker = models.CharField()
    stroke = models.CharField()
    diabetic = models.CharField()
    regEx = models.CharField()
    alcoholic = models.CharField()
    fruits = models.CharField()
    veggies = models.CharField()
    noDoc= models.CharField()
    AnyHealthcare = models.CharField()
    sex = models.CharField()
    bmi = models.IntegerField()


