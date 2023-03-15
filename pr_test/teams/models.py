from django.db import models


class Team(models.Model):
    palettes = models.ManyToManyField(
        "palettes.Palette", blank=True, related_name="teams"
    )
