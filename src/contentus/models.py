from django.db import models
class Contentus(models.Model):
     name = models.CharField(default='',max_length=20)
     email = models.CharField(default='',max_length=20)
     tel = models.IntegerField(default='')
     subject = models.CharField(default='',max_length=50)
     message = models.CharField(default='',max_length=200)


# Create your models here.
