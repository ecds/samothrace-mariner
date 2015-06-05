from samothrace.apps.sites.models import Site
from rest_framework import viewsets
from samothrace.apps.sites.serializers import SiteSerializer


class SiteViewSet(viewsets.ModelViewSet):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer
