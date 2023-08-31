from django.db import models

# Create your models here.

# model are not proper 

class student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)



    
    
