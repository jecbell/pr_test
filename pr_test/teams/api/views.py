from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from pr_test.teams.api.serializers import TeamSerializer
from pr_test.teams.models import Team


class TeamViewSet(CreateModelMixin, ListModelMixin, GenericViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    def get_queryset(self):
        return self.request.user.teams.all()

    @action(detail=True, methods=["post"])
    def join(self, request, pk=None):
        team = Team.objects.get(pk=pk)
        team.users.add(request.user)
        return Response(status=status.HTTP_204_NO_CONTENT)
