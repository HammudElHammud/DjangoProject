from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from .models import Forslar, Category,Images,Comment
class ProductImagesInline(admin.StackedInline):
    model = Images
    extra = 4

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','stats']
    list_filter = ['stats']

class FordslarAdmin(admin.ModelAdmin):
    list_display = ['name','category','pric', 'image_tag','amount']
    readonly_fields = ['image_tag']
    list_filter = ['stats','category']
    inlines = [ProductImagesInline]

class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title','product','image_tag']
    readonly_fields = ['image_tag']


class CategoryAdmin2(DraggableMPTTAdmin):
    mptt_indent_field = "name"
    list_display = ('tree_actions', 'indented_title',
                    'related_products_count', 'related_products_cumulative_count')
    list_display_links = ('indented_title',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Category.objects.add_related_count(
                qs,
                Forslar,
                'category',
                'products_cumulative_count',
                cumulative=True)

        # Add non cumulative product count
        qs = Category.objects.add_related_count(qs,
                 Forslar,
                 'category',
                 'products_count',
                 cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count
    related_products_count.short_description = 'Related products (for this specific category)'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count
    related_products_cumulative_count.short_description = 'Related products (in tree)'

class CommentAdmin(admin.ModelAdmin):
    list_display = ['subject','comment','product' ,'user','status']
    list_filter = ['status']


admin.site.register (Category,CategoryAdmin2)
admin.site.register (Forslar,FordslarAdmin)
admin.site.register (Images,ImagesAdmin)
admin.site.register (Comment,CommentAdmin)


# Register your models here.
