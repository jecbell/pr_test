from django.conf import settings
from django.contrib.postgres.fields import ArrayField
from django.db import models


class Palette(models.Model):
    name = models.CharField(max_length=255)
    colors = ArrayField(models.CharField(max_length=255))
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="palettes"
    )

    def __str__(self):
        return self.name
