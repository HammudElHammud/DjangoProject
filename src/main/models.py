from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Main(models.Model):
    name = models.CharField(max_length=15)
    about  = models.TextField(max_length=10000)
    picurl= models.TextField(max_length=22 ,default="" )
    picname = models.TextField(max_length=22  , default="")
    pagefa  = models.CharField(max_length=15)
    pagetw  = models.CharField(max_length=15)
    pageyt  = models.CharField(max_length=15)
    pageLink  = models.CharField(max_length=15)
    pageTe = models.CharField(max_length=20,default=0)

    name_set = models.CharField(max_length=20,default='-')
    def __str__(self):
        return self.name_set + "  ||"  +str(self.pk)
