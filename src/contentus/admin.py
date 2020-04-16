from django.contrib import admin
from .models import Contentus

class adminContan(admin.ModelAdmin):
    list_display = ['name','email','tel','subject']


admin.site.register(Contentus,adminContan)

# Register your models here.
