from django.urls import path
from apps.task1.api_endpoints.User.UserRegister.views import UserRegisterViewSet
from apps.task1.api_endpoints.User.UserLogin.views import UserLoginViewSet
from apps.task1.api_endpoints.User.UserDelete.views import UserDeleteViewSet

urlpatterns = [
    path("register/", UserRegisterViewSet.as_view({"post": "create"}), name="register"),
    path("login/", UserLoginViewSet.as_view({"post": "login"}), name="login"),
    path(
        "delete/<int:pk>/",
        UserDeleteViewSet.as_view({"delete": "delete"}),
        name="delete",
    ),
]
