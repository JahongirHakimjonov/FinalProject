from django.contrib import admin

from apps.task4.models import Sport, Team, Player, Match, Goal, Card, Substitution


@admin.register(Sport)
class SportAdmin(admin.ModelAdmin):
    list_display = ["name", "description"]
    search_fields = ["name"]


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ["name", "country", "coach", "established_date"]
    search_fields = ["name", "country"]
    list_filter = ["established_date"]


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "team",
        "nationality",
        "position",
        "date_of_birth",
        "height",
        "weight",
    ]
    search_fields = ["name", "team__name"]
    list_filter = ["team", "nationality", "position", "date_of_birth"]


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = [
        "home_team",
        "away_team",
        "date",
        "result",
        "score_home_team",
        "score_away_team",
        "match_location",
        "match_status",
    ]
    search_fields = ["home_team__name", "away_team__name"]
    list_filter = ["date", "result", "match_location"]


@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ["match", "scorer", "minute"]
    search_fields = ["match__home_team__name", "match__away_team__name", "scorer__name"]
    list_filter = ["match", "scorer", "minute"]


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ["match", "player", "card_type", "minute"]
    search_fields = ["match__home_team__name", "match__away_team__name", "player__name"]
    list_filter = ["match", "player", "card_type", "minute"]


@admin.register(Substitution)
class SubstitutionAdmin(admin.ModelAdmin):
    list_display = ["match", "player_out", "player_in", "minute"]
    search_fields = [
        "match__home_team__name",
        "match__away_team__name",
        "player_out__name",
        "player_in__name",
    ]
    list_filter = ["match", "player_out", "player_in"]
