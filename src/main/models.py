from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Main(models.Model):
    # STATUS = (
    #     ('True', 'Evet'),
    #     ('False', 'Hayir'),
    #
    # )
    name = models.CharField(default='', max_length=40)
    # stats = models.CharField(default='', max_length=40, choices=STATUS)

    # title = models.CharField(max_length=15)
    about  = models.TextField(max_length=10000)
    # keyword = models.TextField(max_length=10000)
    # description  = models.TextField(max_length=10000)
    # company  = models.TextField(max_length=10000)
    picurl= models.TextField(max_length=22 ,default="" )
    picname = models.TextField(max_length=22  , default="")
    # smtpserver  = models.CharField(max_length=44)
    # smtpemail  = models.CharField(max_length=44)
    # smtpPassword = models.CharField(max_length=15)
    # smtpPort  = models.CharField(max_length=15)
    pagefa  = models.CharField(max_length=15)
    pagetw  = models.CharField(max_length=15)
    pageyt  = models.CharField(max_length=15)
    pageLink  = models.CharField(max_length=15)
    pageTe = models.CharField(max_length=20,default=0)
    # icon  = models.ImageField(blank=True,upload_to='images/')


    name_set = models.CharField(max_length=20,default='-')
    def __str__(self):
        return self.name_set + "  ||"  +str(self.pk)
