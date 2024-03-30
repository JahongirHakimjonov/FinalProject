from django.contrib import admin
from apps.task3.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("encrypted_price", "encrypted_marja", "package_code")
    exclude = ("encrypted_price", "encrypted_marja")
