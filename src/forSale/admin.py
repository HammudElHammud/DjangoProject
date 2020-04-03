from django.contrib import admin
from .models import Forslar, Category,Images
class ProductImagesInline(admin.StackedInline):
    model = Images
    extra = 4

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','stats']
    list_filter = ['stats']

class FordslarAdmin(admin.ModelAdmin):
    list_display = ['name','categoryadmin','pric', 'image_tag','amount']
    readonly_fields = ['image_tag']
    list_filter = ['stats','categoryadmin']
    inlines = [ProductImagesInline]

class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title','product','image_tag']
    readonly_fields = ['image_tag']



admin.site.register (Category,CategoryAdmin)
admin.site.register (Forslar,FordslarAdmin)
admin.site.register (Images,ImagesAdmin)


# Register your models here.
