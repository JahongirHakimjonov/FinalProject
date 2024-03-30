from rest_framework import serializers
from apps.task1.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password", "is_deleted"]
        extra_kwargs = {"password": {"write_only": True}}
