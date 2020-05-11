from django.contrib import admin
from .models import Main, UserProfile
from django.contrib.auth.models import User


class UserProfilAdmin(admin.ModelAdmin):
    list_display = [  'phone','address' ,'image_tag','phone']






admin.site.register (Main)
admin.site.register(UserProfile,UserProfilAdmin)
