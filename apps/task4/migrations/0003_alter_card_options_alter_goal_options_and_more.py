# Generated by Django 5.0.3 on 2024-03-29 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("task4", "0002_match_player_sport_team_goal_card_player_team_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="card",
            options={"verbose_name_plural": "Cards"},
        ),
        migrations.AlterModelOptions(
            name="goal",
            options={"verbose_name_plural": "Goals"},
        ),
        migrations.AlterModelOptions(
            name="match",
            options={"verbose_name_plural": "Matches"},
        ),
        migrations.AlterModelOptions(
            name="player",
            options={"verbose_name_plural": "Players"},
        ),
        migrations.AlterModelOptions(
            name="sport",
            options={"verbose_name_plural": "Sports"},
        ),
        migrations.AlterModelOptions(
            name="team",
            options={"verbose_name_plural": "Teams"},
        ),
        migrations.AlterModelTable(
            name="card",
            table="cards",
        ),
        migrations.AlterModelTable(
            name="goal",
            table="goals",
        ),
        migrations.AlterModelTable(
            name="match",
            table="matches",
        ),
        migrations.AlterModelTable(
            name="player",
            table="players",
        ),
        migrations.AlterModelTable(
            name="sport",
            table="sports",
        ),
        migrations.AlterModelTable(
            name="team",
            table="teams",
        ),
    ]