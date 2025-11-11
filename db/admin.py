from django.contrib import admin
from .models import Product, User


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('upc', 'name', 'price')
    search_fields = ('upc', 'name')


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
