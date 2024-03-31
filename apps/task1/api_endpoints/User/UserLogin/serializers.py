from rest_framework import serializers
from apps.task1.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", "password"]
        # extra_kwargs = {"password": {"write_only": True}}
