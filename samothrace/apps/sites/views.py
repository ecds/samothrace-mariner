from django.shortcuts import render
import csv
from djqscsv import render_to_csv_response
from django.db.models import Q
from samothrace.apps.sites.models import Site, Marker, Koina
from rest_framework import viewsets
from samothrace.apps.sites.serializers import SiteSerializer, MarkerSerializer, KoinaSerializer
from samothrace.apps.sites.models import Site, Marker, Koina, Ancient_Sources
from samothrace.apps.argonautica.models import Person, Stops, Places_Referenced
from samothrace.apps.people.models import Individual, Role, Priesthood
from samothrace.apps.inscriptions.models import Inscription
from django_mysql.models import GroupConcat

class SiteViewSet(viewsets.ModelViewSet):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer


class MarkerViewSet(viewsets.ModelViewSet):
    queryset = Marker.objects.all()
    serializer_class = MarkerSerializer


class KoinaViewSet(viewsets.ModelViewSet):
    queryset = Koina.objects.all()
    serializer_class = KoinaSerializer


def Inscriptions_Nodes(request):
    InscriptionSiteData = Site.objects.values('site_id', 'name', 'latitude', 'longitude', 'inscription__name', 'inscription__start_date', 'inscription__end_date', 'inscription__individual__individual_id', 'inscription__individual__name', 'inscription__individual__role__title').filter(inscription__name__isnull=False).order_by('name')
    return render_to_csv_response(InscriptionSiteData, field_header_map={'site_id': 'Id', 'name': 'name', 'latitude': 'latitude', 'longitude': 'longitude', 'inscription__name':'inscription', 'inscription__start_date':'start date', 'inscription__end_date':'end date', 'inscription__individual__individual_id':'individual', 'inscription__individual__name':'name', 'inscription__individual__role__title':'role'})

#def Inscriptions_NodesDistinct(request):
#    InscriptionSiteDataDistinct = Site.objects.values('site_id', 'name', 'latitude', 'longitude').filter(inscription__name__isnull=False).annotate(Inscription=GroupConcat('inscription__name', distinct=True), Inscription_Start=GroupConcat('inscription__start_date', distinct=True), Inscription_End=GroupConcat('inscription__end_date', dintinct=True), Individual=GroupConcat('inscription__individual__individual_id', dintinct=True), IndividualName=GroupConcat('inscription__individual__name', distinct=True), IndividualRole=GroupConcat('inscription__individual__role__title', distinct=False)).order_by('name')
#    return render_to_csv_response(InscriptionSiteDataDistinct, field_header_map={'site_id': 'Id', 'name': 'name', 'latitude': 'latitude', 'longitude': 'longitude', 'Inscription':'inscription', 'Inscription_Start':'start date', 'Inscription_End':'end date', 'Individual':'individual', 'IndividualName':'name', 'IndividualRole':'role'})

