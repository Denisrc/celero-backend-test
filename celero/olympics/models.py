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

class Athlete(models.Model):
    name = models.CharField(blank=False, max_length=200, null=False)
    age = models.PositiveSmallIntegerField()
    height = models.PositiveSmallIntegerField()
    weight = models.PositiveSmallIntegerField()
    sex = models.CharField(blank=False, max_length=1, choices=SEX, null=False)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)