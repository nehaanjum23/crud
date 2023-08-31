from django.db import models

# Create your models here.

# model are not proper 

class student(models.Model):
    name=models.CharField(max_length=100)
    roll=models.IntegerField()
    city=models.CharField(max_length=100)

class studentemail(models.Model):
    name=models.CharField(max_length=256)
    email=models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True
    )


    
    
