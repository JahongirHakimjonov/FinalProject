from django.contrib import admin
from apps.task2.models import Vacancy


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "salary"]
    search_fields = ["title", "description"]
    list_filter = ["salary"]
