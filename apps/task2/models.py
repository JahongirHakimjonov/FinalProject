from django.db import models
from apps.shared.models import AbstractModel


class Vacancy(AbstractModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = "vacancies"
        verbose_name = "Vacancy"
        verbose_name_plural = "Vacancies"

    def __str__(self):
        return self.title
