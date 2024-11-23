from django.db import models

# Create your models here.
class Employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField()
    esal=models.FloatField()
    eaddr=models.CharField()