from __future__ import unicode_literals

from django import forms
from django.contrib.auth.models import User
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
from django.utils.safestring import mark_safe


class Main(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayir'),

    )
    name = models.CharField(default='', max_length=40)
    status = models.CharField(default='', max_length=40, choices=STATUS)

    title = models.CharField(max_length=15)
    about  = RichTextUploadingField()
    keyword = models.TextField(max_length=10000)
    description  = models.TextField(max_length=10000)
    company  = models.TextField(max_length=10000)
    smtpserver  = models.CharField(max_length=44)
    smtpemail  = models.CharField(max_length=44)
    smtpPassword = models.CharField(max_length=15)
    smtpPort  = models.CharField(max_length=15)
    pagefa  = models.CharField(max_length=15)
    pagetw  = models.CharField(max_length=15)
    pageyt  = models.CharField(max_length=15)
    pageLink  = models.CharField(max_length=15)
    pageTe = models.CharField(max_length=20,default=0)
    icon  = models.ImageField(blank=True,upload_to='images/')


    name_set = models.CharField(max_length=20,default='-')
    def __str__(self):
        return self.name_set + "  ||"  +str(self.pk)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(blank=True,max_length=20)
    address = models.CharField(blank=True,max_length=202)
    city = models.CharField(blank=True,max_length=20)
    country= models.CharField(blank=True,max_length=20)
    image = models.ImageField(upload_to="images/profile_images/", blank=True)

    def __str__(self):
        return self.user.username



    @property
    def use_name(self):
        return self.user.usernames

    @property
    def image_tag(self):
        if self.image is None:
            return ''
        self.image.short_description = 'Image'
        return mark_safe('<img src="{}" width="50" height="50" />'.format(self.image.url))


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone', 'address', 'city', 'country','image')




