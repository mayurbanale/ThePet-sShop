from django.contrib import admin

from .models import category, product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']
    list_filter = ['name']


admin.site.register(category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'description']
    list_filter = ['price', 'category']


admin.site.register(product, ProductAdmin)
