from rest_framework import serializers

from pr_test.palettes.models import Palette


class PaletteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Palette
        fields = ["id", "name", "colors"]
