from django.db.models import Q
from django.views.generic import View, ListView, DetailView
from samothrace.apps.sites.models import Site, Marker, Koina
from rest_framework import viewsets
from samothrace.apps.sites.serializers import SiteSerializer, MarkerSerializer, KoinaSerializer
from samothrace.apps.people.models import Individual
from samothrace.apps.inscriptions.models import Inscription


class SiteList(ListView):
    'List all Sites'
    model = Site


class SiteDetail(DetailView):
    'Display details for a single site'
    model = Site

    def get_context_data(self, **kwargs):
        #h/t http://stackoverflow.com/a/14936328
        context = super(SiteDetail, self).get_context_data(**kwargs)
        context["individuals"] = Individual.objects.filter(site=self.object.pk)
        context["inscriptions"] = Inscription.objects.filter(find_spot=self.object.pk)
        return context



    
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
