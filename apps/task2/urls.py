from django.urls import path
from apps.task2.api_endpoints.Vacancy.VacancyFilter.views import VacancyFilterAPIView

urlpatterns = [
    path('vacancies/', VacancyFilterAPIView.as_view(), name='vacancy-filter'),
]
