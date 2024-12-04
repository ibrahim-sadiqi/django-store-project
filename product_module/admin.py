from django.contrib import admin
from .models import Product


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    #readonly_fields = ['rating']
    prepopulated_fields = {
        'slug': ['title']
    }

    list_display = ['title', 'price', 'rating', 'is_active']
    list_filter = ['rating', 'is_active']
    list_editable = ['rating', 'is_active']


admin.site.register(Product, ProductAdmin)
