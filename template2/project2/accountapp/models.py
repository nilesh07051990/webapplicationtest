from django.db import models

# Create your models here.
class CreateAccount(models.Model):
    cid=models.IntegerField()
    name=models.CharField(max_length=20)
    address=models.CharField(max_length=30)
    salary=models.IntegerField()
    mobile=models.BigIntegerField(max_length=20)

