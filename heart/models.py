from django.db import models


# Create your models here.
class Person(models.Model):
    email = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    passphrase = models.CharField(max_length=500)

class FormSubmission(models.Model):
    age = models.IntegerField()
    highBP = models.IntegerField()
    highChol = models.IntegerField()
    smoker = models.IntegerField()
    stroke = models.IntegerField()
    diabetic = models.IntegerField()
    diffWalk = models.IntegerField()
    mentalHlth = models.IntegerField()
    genHlth = models.IntegerField()
    physHlth = models.IntegerField()
    regEx = models.IntegerField()
    bmi = models.IntegerField()
    prediction = models.FloatField()
    condition = models.CharField()


