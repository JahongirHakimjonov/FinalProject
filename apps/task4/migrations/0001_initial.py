# Generated by Django 5.0.3 on 2024-03-29 15:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Sports",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=100)),
            ],
            options={
                "verbose_name": "Sport",
                "verbose_name_plural": "Sports",
                "db_table": "sports",
            },
        ),
        migrations.CreateModel(
            name="SportEvent",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("match_time", models.DateTimeField()),
                ("match_location", models.CharField(max_length=100)),
                ("team1", models.CharField(max_length=100)),
                ("team2", models.CharField(max_length=100)),
                ("team1_score", models.IntegerField(default=0)),
                ("team2_score", models.IntegerField(default=0)),
                ("winner", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "match_status",
                    models.CharField(
                        choices=[
                            ("Not Started", "Not Started"),
                            ("In Progress", "In Progress"),
                            ("Completed", "Completed"),
                        ],
                        default="Not Started",
                        max_length=100,
                    ),
                ),
                (
                    "match_result",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "sport",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="task4.sports"
                    ),
                ),
            ],
            options={
                "verbose_name": "Sport Event",
                "verbose_name_plural": "Sport Events",
                "db_table": "sport_events",
            },
        ),
    ]