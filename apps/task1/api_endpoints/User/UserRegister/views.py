from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from apps.task1.api_endpoints.User.UserRegister.serializers import (
    UserRegisterSerializer,
)

from apps.task1.models import User


class UserRegisterViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            if user:
                headers = self.get_success_headers(serializer.data)
                return Response(
                    serializer.data, status=status.HTTP_201_CREATED, headers=headers
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=["post"])
    def set_password(self, request, pk=None):
        user = self.get_object()
        password = request.data.get("password")
        if password:
            user.set_password(password)
            user.save()
            return Response({"status": "password set"}, status=status.HTTP_200_OK)
        else:
            return Response(
                {"error": "Password is not provided"},
                status=status.HTTP_400_BAD_REQUEST,
            )


__all__ = ["UserRegisterViewSet"]
