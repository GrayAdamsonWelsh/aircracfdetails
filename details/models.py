from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

# Create your models here.

class Type(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name 

    def get_absolute_url(self):
        return reverse("home")


class Post(models.Model):
    title = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=50, default="")
    firstFlight = models.DateField(default='1900-01-01')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=30, default="")
    introduction = models.DateField(default='1900-01-01')
    numberBuilt = models.IntegerField(default=0)
    history = models.TextField()
    origin = models.CharField(max_length=255, default="")
    post_date = models.DateField(auto_now_add=True) 
    type = models.CharField(max_length=50, default="GA")

    def __str__(self):
        return self.title + '¦' + str(self.author)

    def get_absolute_url(self):
        return reverse("home")
