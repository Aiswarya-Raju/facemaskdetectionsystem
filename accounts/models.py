from django.db import models

# Create your models here.
class loginm(models.Model):
 Username=models.CharField( max_length=30)
password=models.CharField(max_length=20)
