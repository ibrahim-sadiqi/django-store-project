from django.contrib import admin
from .models import Product, ProductCategory, ProductTag


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['price', 'is_active', 'is_delete']
    list_filter = ['category', 'is_active']


admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(ProductTag)