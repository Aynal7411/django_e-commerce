from django.contrib import admin
from .models import RiceCategory, Product

# Rice Category Admin
@admin.register(RiceCategory)
class RiceCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

# Product Admin
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock', 'created_at', 'updated_at')
    list_filter = ('category', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    list_editable = ('price', 'stock')
    ordering = ('-created_at',)
