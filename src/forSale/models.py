from __future__ import unicode_literals
from django.db import models
class Forslar(models.Model):
    name = models.CharField(default='',max_length=40)
    stats = models.CharField(default='',max_length=40)
    category = models.CharField(default='',max_length=40)
    pric  = models.IntegerField(default='')
    size = models.CharField(default='',max_length= 40)
    picurl = models.TextField(max_length=50, default="")
    picname = models.TextField(max_length=50, default="")
    description = models.CharField(max_length=200,default="")


# Create your models here.
