from django.contrib import admin

from .models import ShopCart,Order,OrderProduct

class ShopCartAdmin(admin.ModelAdmin):
    list_display = ['user','product','quantity','price','amount']
    list_filter = ['user']

class OrderProductline(admin.TabularInline):
    model = OrderProduct
    readonly_fields = ('user','product','price','quantity','amount')
    can_delete = False
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','phone','country','city']
    list_filter = ['status']
    readonly_fields = ('user','last_name','address','city','country','ip','total','phone')
    inlines = [OrderProductline]

class OrderProductAdmin(admin.ModelAdmin):
    list_filter = ['user']
    list_display = ['user','price','product','quantity','amount']



admin.site.register(ShopCart,ShopCartAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderProduct,OrderProductAdmin)


# Register your models here.
