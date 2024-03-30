from rest_framework import serializers
from apps.task3.models import Product


class ProductSerializer(serializers.ModelSerializer):
    encrypted_price = serializers.SerializerMethodField()
    encrypted_marja = serializers.SerializerMethodField()
    encrypted_package_code = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            "price",
            "marja",
            "package_code",
            "encrypted_price",
            "encrypted_marja",
            "encrypted_package_code",
        ]

    def get_encrypted_price(self, obj):
        return obj.encrypted_price

    def get_encrypted_marja(self, obj):
        return obj.encrypted_marja

    def get_encrypted_package_code(self, obj):
        return obj.package_code
