from rest_framework import serializers
from apps.task1.models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", "email", "password"]

    def create(self, validated_data):
        username = validated_data["username"]
        password = validated_data["password"]
        email = validated_data.get("email")

        user = User.objects.create(username=username, email=email)
        user.set_password(password)
        user.save()
        return user
