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

        user = User.objects.filter(username=username).first()
        if user:
            if user.is_deleted:
                user.restore()
                user.email = email
                user.set_password(password)
                user.save()
            else:
                raise serializers.ValidationError(
                    "A user with that username already exists."
                )
        else:
            user = User.create_user(username=username, password=password, email=email)

        return user
