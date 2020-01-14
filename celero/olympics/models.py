from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
SEASONS = [
    ("S", "Summer"), 
    ("W", "Winter")
]

SEX = [
    ("M", "Male"),
    ("F", "Female")
]

MEDALS = [
    ("G", "Gold"),
    ("S", "Silver"),
    ("B", "Bronze")
]

class Sport(models.Model):
    name = models.CharField(blank=False, max_length=100, null=False, unique=True)

class Event(models.Model):
    name = models.CharField(blank=False, max_length=100, null=False)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)

class Olympic(models.Model):
    year = models.PositiveSmallIntegerField(
        blank=False, 
        null=False, 
        validators=[MinValueValidator(1896), MaxValueValidator(32767)]
    )
    season = models.CharField(blank=False, max_length=1, choices=SEASONS, null=False)
    city = models.CharField(blank=False, max_length=100, null=False)
    
class Team(models.Model):
    noc = models.CharField(blank=False, max_length=3, null=False, unique=True)
    name = models.CharField(blank=False, max_length=100, null=False)
    notes = models.CharField(max_length=100, default=None, null=True)

class Athlete(models.Model):
    name = models.CharField(blank=False, max_length=200, null=False)
    sex = models.CharField(blank=False, max_length=1, choices=SEX, null=False)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

class OlympicEvent(models.Model):
    medal = models.CharField(max_length=1, choices=MEDALS, null=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    olympic = models.ForeignKey(Olympic, on_delete=models.CASCADE)
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE)
    age = models.PositiveSmallIntegerField(default=None)
    height = models.PositiveSmallIntegerField(default=None)
    weight = models.PositiveSmallIntegerField(default=None)