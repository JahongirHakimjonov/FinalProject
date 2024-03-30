from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from apps.task1.models import User
from apps.task1.api_endpoints.User.UserDelete.serializers import UserSerializer


class UserDeleteViewSet(viewsets.ViewSet):
    serializer_class = UserSerializer

    @action(detail=True, methods=["delete"])
    def delete(self, request, pk=None):
        user = User.objects.filter(pk=pk).first()
        if user and not user.is_deleted:
            user.soft_delete()
            user.save()
            return Response({"message": "User deleted"})
        return Response({"message": "User not found"})


__all__ = ["UserDeleteViewSet"]
