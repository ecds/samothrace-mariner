from samothrace.apps.sites.models import Site, Marker, Koina
from rest_framework import viewsets
from samothrace.apps.sites.serializers import SiteSerializer, MarkerSerializer, KoinaSerializer


class SiteViewSet(viewsets.ModelViewSet):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer


class MarkerViewSet(viewsets.ModelViewSet):
    queryset = Marker.objects.all()
    serializer_class = MarkerSerializer


class KoinaViewSet(viewsets.ModelViewSet):
    queryset = Koina.objects.all()
    serializer_class = KoinaSerializer
