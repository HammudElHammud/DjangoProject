from __future__ import unicode_literals
from django.db import models
from django.forms import ModelForm
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from mptt.models import MPTTModel, TreeForeignKey
from ckeditor_uploader.fields import RichTextUploadingField




class Category(MPTTModel):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayir'),

    )
    name= models.CharField(default='', max_length=40)
    stats = models.CharField(default='', max_length=40, choices=STATUS)
    keyword = models.CharField(default='', max_length=40)
    description = models.CharField(max_length=200, default="")
    image = models.ImageField(blank=True,upload_to='images/')
    slug = models.SlugField()
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    # parent = TreeForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    # createAt = models.DateTimeField(auto_now_add=True)
    # updateAt = models.DateTimeField(auto_now=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        full_path  = [self.name]
        k = self.parent
        while k is not  None:
            full_path.append(k.name)
            k = k.parent
        return  '>>'  .join(full_path[ :: -1])

    def children(self):
        return Category.objects.filter(parent=self).all().all()

    def image_tag(self):
        return mark_safe('<img src="{}" width="50" height="50" />'.format(self.image.url))
    image_tag.short_description = 'Image'







class Forslar(models.Model):
    STATUS = (
        ('True','Evet'),
        ('False','Hayir'),

    )
    userOwner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(default='',max_length=40)
    stats = models.CharField(default='',max_length=40,choices=STATUS)
    # category = models.CharField(default='',max_length=40)
    category = models.ForeignKey('Category',on_delete=models.CASCADE, null=True, blank=True)
    pric  = models.IntegerField(default=0)
    amount  = models.IntegerField(default='')
    image = models.ImageField(blank=True,upload_to='images/',null=False)
    size = models.CharField(default='',max_length= 40)

    # picurl = models.TextField(max_length=50, default="")
    # picname = models.TextField(max_length=50, default="")
    description = RichTextUploadingField()
    detail = RichTextUploadingField()

    slug = models.SlugField()
    parent = models.ForeignKey('self', blank= True,null=True,related_name='children',on_delete=models.CASCADE)
    # createAt = models.DateField(default=timezone.now())
    # updateAt = models.DateField(default=timezone.now())
    def __str__(self):
        return self.name

    @property
    def image_tag(self):
        if self.image is None:
            return ''
        self.image.short_description = 'Image'
        return mark_safe('<img src="{}" width="50" height="50" />'.format(self.image.url))

    @property
    def images(self):
        return Images.objects.filter(product=self)

class Images(models.Model):
    product = models.ForeignKey(Forslar,on_delete=models.CASCADE)
    title = models.CharField(max_length=22)
    image = models.ImageField(blank=True,upload_to='images/')
    def __str__(self):
        return self.title
    def image_tag(self):
        return mark_safe('<img src="{}" width="50" height="50" />'.format(self.image.url))
    image_tag.shovrt_description = 'Image'


class Comment(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayir'),

    )
    user = models.ForeignKey(User, on_delete=models.CASCADE ,null=True ,blank=True)
    status = models.CharField(default='', max_length=40, choices=STATUS)
    product = models.ForeignKey(Forslar,on_delete=models.CASCADE,null=True ,blank=True)
    subject =  models.TextField(max_length=80,blank=True)
    comment =  models.TextField(max_length=200,blank=True)
    rate = models.IntegerField(blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.subject


# class CommentForm(ModelForm):
#     class Meta:
#         model = Comment
#         fields = ['subject','comment','rate']










# Create your models here.
