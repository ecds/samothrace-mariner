from django.views.generic import View, ListView, DetailView
from samothrace.apps.sites.models import Site, Marker, Koina
from rest_framework import viewsets
from samothrace.apps.sites.serializers import SiteSerializer, MarkerSerializer, KoinaSerializer


class SiteList(ListView):
    'List all Journals'
    model = Site

class SiteDetail(DetailView):
    'Display details for a single site'
    model = Site



    
# REST Framework--------------------------  
class SiteViewSet(viewsets.ModelViewSet):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer


class MarkerViewSet(viewsets.ModelViewSet):
    queryset = Marker.objects.all()
    serializer_class = MarkerSerializer


class KoinaViewSet(viewsets.ModelViewSet):
    queryset = Koina.objects.all()
    serializer_class = KoinaSerializer
