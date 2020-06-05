from django.contrib import admin
from .models import Main, UserProfile, FAQ
from django.contrib.auth.models import User


class UserProfilAdmin(admin.ModelAdmin):
    list_display = [  'phone','address' ,'image_tag','phone']


class FAQAdmin(admin.ModelAdmin):
    list_display = ['orderNumber', 'question','answer','status']
    list_filter = ['status']




admin.site.register (Main)
admin.site.register(UserProfile,UserProfilAdmin)
admin.site.register(FAQ,FAQAdmin)
