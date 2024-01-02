from django.db import models


# Create your models here.
from app.models import *

class Topic(models.Model):
    tname=models.CharField(max_length=100,primary_key=True)

    def __str__(self):
        return self.tname
    
class Webpage(models.Model):
    tname=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    url=models.URLField()


    def __str__(self):
        return self.name
    

class AccessRecord(models.Model):
    name=models.ForeignKey(Webpage,on_delete=models.CASCADE)
    author=models.CharField(max_length=100)
    date=models.DateField()

    def __str__(self):
        return self.author

