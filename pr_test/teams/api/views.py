from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet

from pr_test.teams.api.serializers import TeamSerializer
from pr_test.teams.models import Team


class TeamViewSet(CreateModelMixin, ListModelMixin, GenericViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    def get_queryset(self):
        return self.request.user.teams.all()
