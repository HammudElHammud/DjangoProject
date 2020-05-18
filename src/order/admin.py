from django.contrib import admin

from order.models import ShopCart

class ShopCartAdmin(admin.ModelAdmin):
    list_display = ['user','product','quantity','price','amount']
    list_filter = ['user']

admin.site.register(ShopCart,ShopCartAdmin)


# Register your models here.
