from django.db import models
from apps.shared.models import AbstractModel


class Sport(AbstractModel):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Sports"
        db_table = "sports"


class Team(AbstractModel):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    coach = models.CharField(max_length=100)  # Murabbiy
    established_date = models.DateField()
    logo = models.ImageField(upload_to="team_logos/", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Teams"
        db_table = "teams"


class Player(AbstractModel):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    height = models.DecimalField(max_digits=4, decimal_places=2)
    weight = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Players"
        db_table = "players"


class Match(AbstractModel):
    RESULT_CHOICES = (
        ("Home Win", "Home Win"),
        ("Away Win", "Away Win"),
        ("Draw", "Draw"),
    )
    MATCH_STATUS = (
        ("Not started", "Not started"),
        ("In progress", "In progress"),
        ("Finished", "Finished"),
    )

    home_team = models.ForeignKey(
        Team, related_name="home_matches", on_delete=models.CASCADE
    )
    away_team = models.ForeignKey(
        Team, related_name="away_matches", on_delete=models.CASCADE
    )
    date = models.DateField()
    result = models.CharField(max_length=10, choices=RESULT_CHOICES, blank=True)
    score_home_team = models.IntegerField(default=0)
    score_away_team = models.IntegerField(default=0)
    match_location = models.CharField(max_length=100)
    match_status = models.CharField(
        max_length=20, choices=MATCH_STATUS, default="Not started"
    )

    def __str__(self):
        return f"{self.home_team} vs {self.away_team} - {self.date}"

    class Meta:
        verbose_name_plural = "Matches"
        db_table = "matches"


class Goal(AbstractModel):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    scorer = models.ForeignKey(Player, on_delete=models.CASCADE)
    minute = models.IntegerField()

    def __str__(self):
        return f"{self.scorer} scored in {self.minute}'"

    class Meta:
        verbose_name_plural = "Goals"
        db_table = "goals"


class Card(AbstractModel):
    CARD_CHOICES = (
        ("Yellow", "Yellow"),
        ("Red", "Red"),
    )
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    card_type = models.CharField(max_length=10, choices=CARD_CHOICES)
    minute = models.IntegerField()

    def __str__(self):
        return f"{self.player} - {self.card_type}"

    class Meta:
        verbose_name_plural = "Cards"
        db_table = "cards"
