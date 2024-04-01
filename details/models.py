from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    history = models.TextField()
    origin = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.title + '¦' + str(self.author)

    def get_absolute_url(self):
        return reverse("home")
