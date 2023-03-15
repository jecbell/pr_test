import re

from rest_framework import serializers

from pr_test.palettes.models import Palette


class PaletteSerializer(serializers.ModelSerializer):
    hex_regex = r"^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$"

    class Meta:
        model = Palette
        fields = ["id", "name", "colors"]

    def validate_colors(self, colors):
        invalid_colors = [
            color for color in colors if not re.match(self.hex_regex, color)
        ]
        if invalid_colors:
            raise serializers.ValidationError(f"Invalid colors: {invalid_colors}")
        return colors
