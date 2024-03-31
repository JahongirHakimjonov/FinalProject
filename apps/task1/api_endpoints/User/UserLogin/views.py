from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from apps.task1.models import User
from apps.task1.api_endpoints.User.UserLogin.serializers import UserSerializer


class UserLoginViewSet(viewsets.ViewSet):
    serializer_class = UserSerializer

    @swagger_auto_schema(request_body=UserSerializer)
    @action(detail=False, methods=["post"])
    def login(self, request):
        data = request.data
        username = data.get("username", "")
        password = data.get("password", "")
        user = User.objects.filter(username=username, is_deleted=False).first()

        if user and user.check_password(password):
            return Response({"message": "Successful login"})
        return Response({"message": "Invalid credentials"})


__all__ = ["UserLoginViewSet"]
