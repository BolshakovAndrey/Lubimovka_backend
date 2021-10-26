from rest_framework import mixins, viewsets

from apps.library.models import Play
from apps.library.serializers import PlaySerializer


class PlaysAPIView(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Play.objects.all()
    serializer_class = PlaySerializer
