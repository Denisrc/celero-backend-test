from django.db import models

class Sport(models.Model):
    name = models.CharField(blank=False, max_length=100, null=False, unique=True)