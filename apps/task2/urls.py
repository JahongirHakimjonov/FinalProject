from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.task2.api_endpoints.Vacancy.VacancyFilter.views import VacancyFilterViewSet

router = DefaultRouter()
router.register(r"vacancies", VacancyFilterViewSet, basename="vacancy")

urlpatterns = [
    path("", include(router.urls)),
]
