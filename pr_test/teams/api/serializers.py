from rest_framework import serializers

from pr_test.teams.models import Team


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ("id",)
