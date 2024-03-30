# Generated by Django 5.0.3 on 2024-03-30 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("is_deleted", models.BooleanField(default=False)),
                ("username", models.CharField(max_length=150, unique=True)),
                ("email", models.EmailField(max_length=255)),
                ("password", models.CharField(max_length=128)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
