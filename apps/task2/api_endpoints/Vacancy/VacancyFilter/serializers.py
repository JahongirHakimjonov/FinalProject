from rest_framework import serializers
from apps.task2.models import Vacancy


class VacancyFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ["title", "description", "salary"]
