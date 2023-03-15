from django.contrib.postgres.fields import ArrayField
from django.db import models


class Palette(models.Model):
    name = models.CharField(max_length=255)
    colors = ArrayField(models.CharField(max_length=255))

    def __str__(self):
        return self.name
