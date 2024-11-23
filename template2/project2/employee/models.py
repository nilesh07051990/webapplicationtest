from django.db import models
from timezone_field import TimeZoneField
from django.db import models
# Create your models here.

class Employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=35)
    esal=models.CharField(max_length=35)
    eadd=models.TextField()
    edate=models.DateField(auto_now_add=True)
    timezone=TimeZoneField(default='utc')
