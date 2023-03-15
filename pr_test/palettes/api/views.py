from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet

from pr_test.palettes.api.serializers import PaletteSerializer
from pr_test.palettes.models import Palette


class PaletteViewSet(ListModelMixin, CreateModelMixin, GenericViewSet):
    queryset = Palette.objects.all()
    serializer_class = PaletteSerializer

    def get_queryset(self, *args, **kwargs):
        assert isinstance(self.request.user.id, int)
        return self.queryset.filter(user=self.request.user.id)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
