# Generated by Django 5.0.3 on 2024-03-29 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("task4", "0004_match_match_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="card",
            name="card_type",
            field=models.CharField(
                choices=[("Yellow", "Yellow"), ("Red", "Red")], max_length=10
            ),
        ),
    ]
