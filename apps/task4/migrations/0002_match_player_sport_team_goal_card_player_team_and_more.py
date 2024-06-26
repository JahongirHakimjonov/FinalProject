# Generated by Django 5.0.3 on 2024-03-29 17:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("task4", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Match",
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
                ("date", models.DateField()),
                (
                    "result",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Home Win", "Home Win"),
                            ("Away Win", "Away Win"),
                            ("Draw", "Draw"),
                        ],
                        max_length=10,
                    ),
                ),
                ("score_home_team", models.IntegerField(default=0)),
                ("score_away_team", models.IntegerField(default=0)),
                ("match_location", models.CharField(max_length=100)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Player",
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
                ("nationality", models.CharField(max_length=100)),
                ("position", models.CharField(max_length=50)),
                ("date_of_birth", models.DateField()),
                ("height", models.DecimalField(decimal_places=2, max_digits=4)),
                ("weight", models.DecimalField(decimal_places=2, max_digits=5)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Sport",
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
                ("description", models.TextField()),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Team",
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
                ("country", models.CharField(max_length=100)),
                ("coach", models.CharField(max_length=100)),
                ("established_date", models.DateField()),
                (
                    "logo",
                    models.ImageField(blank=True, null=True, upload_to="team_logos/"),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Goal",
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
                ("minute", models.IntegerField()),
                (
                    "match",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="task4.match"
                    ),
                ),
                (
                    "scorer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="task4.player"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Card",
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
                ("card_type", models.CharField(max_length=10)),
                ("minute", models.IntegerField()),
                (
                    "match",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="task4.match"
                    ),
                ),
                (
                    "player",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="task4.player"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="player",
            name="team",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="task4.team"
            ),
        ),
        migrations.AddField(
            model_name="match",
            name="away_team",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="away_matches",
                to="task4.team",
            ),
        ),
        migrations.AddField(
            model_name="match",
            name="home_team",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="home_matches",
                to="task4.team",
            ),
        ),
        migrations.DeleteModel(
            name="SportEvent",
        ),
        migrations.DeleteModel(
            name="Sports",
        ),
    ]
