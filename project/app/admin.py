from django.contrib import admin
from .models import Shop, Warehouse, Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'sold_out')


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')


@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title')
