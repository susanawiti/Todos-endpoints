from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Post(models.Model):
    userId = models.IntegerField(default= 1)
    tiltle = models.CharField(default="Default Title",max_length = 200)
    body= models.TextField(default='Body of post goes here')
    picture = models.ImageField(default='default.png')
   