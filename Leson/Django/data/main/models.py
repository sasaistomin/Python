from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()


class Auto(models.Model):
    name = models.CharField(max_length=50)
    engine = models.IntegerField()
    ear = models.IntegerField()
    color = models.CharField()