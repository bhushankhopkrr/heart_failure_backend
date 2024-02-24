from django.db import models


# Create your models here.
class Person(models.Model):
    email = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    passphrase = models.CharField(max_length=500)

class FormSubmission(models.Model):
    age = models.IntegerField()
    highBP = models.CharField()
    highChol = models.CharField()
    smoker = models.CharField()
    stroke = models.CharField()
    diabetic = models.CharField()
    diffWalk = models.CharField()
    mentalHlth = models.IntegerField()
    genHlth = models.IntegerField()
    physHlth = models.IntegerField()
    regEx = models.CharField()
    bmi = models.IntegerField()


