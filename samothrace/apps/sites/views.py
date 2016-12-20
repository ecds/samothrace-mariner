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

# gives you nodes of cities where stones were found
#def Inscriptions_Nodes(request):
 #   InscriptionSiteData = Site.objects.values('inscription_id', 'name', 'latitude', 'longitude', 'inscription__name', 'inscription__start_date', 'inscription__end_date').filter(inscription__name__isnull=False).distinct().order_by('name')
 #   return render_to_csv_response(InscriptionSiteData, field_header_map={'inscription_id': 'id', 'name': 'name', 'latitude': 'latitude', 'longitude': 'longitude', 'inscription__name':'inscription', 'inscription__start_date':'start date', 'inscription__end_date':'end date'})

#def Inscriptions_NodesDistinct(request):
#    InscriptionSiteDataDistinct = Site.objects.values('site_id', 'name', 'latitude', 'longitude').filter(inscription__name__isnull=False).annotate(Inscription=GroupConcat('inscription__name', distinct=True), Inscription_Start=GroupConcat('inscription__start_date', distinct=True), Inscription_End=GroupConcat('inscription__end_date', distinct=True)).order_by('name')
#    return render_to_csv_response(InscriptionSiteDataDistinct, field_header_map={'site_id': 'Id', 'name': 'name', 'latitude': 'latitude', 'longitude': 'longitude', 'Inscription':'inscription', 'Inscription_Start':'start date', 'Inscription_End':'end date'})

# gives you nodes of cities where people were from
#def Inscriptions_NodesPeopleSites(request):
#    InscriptionBothSiteData = Site.objects.values('individual_id', 'name', 'latitude', 'longitude', 'individual__name', 'individual__patronym', 'individual__inscription__name', 'individual__inscription__start_date', 'individual__inscription__end_date', 'individual__role__title').filter(individual__inscription__name__isnull=False).distinct().order_by('name')
#    return render_to_csv_response(InscriptionBothSiteData, field_header_map={'individual_id': 'id', 'name': 'name', 'latitude': 'latitude', 'longitude': 'longitude', 'individual__inscription__name':'inscription', 'individual__inscription__start_date':'start date', 'individual__inscription__end_date':'end date', 'individual__name':'individual', 'individual__patronym':'individual patronym', 'individual__role__title':'Roles'})

#def Inscriptions_NodesPeopleSitesDistinct(request)
#    InscriptionPeopleSiteDistinct = Site.objects.values('site_id', 'name', 'latitude', 'longitude').annotate(Individual=GroupConcat('individual__name', distinct=True), Patronym=GroupConcat('individual__patronym', distinct=True), Inscription=GroupConcat('individual__inscription__name', distinct=True), Inscription_Start=GroupConcat('individual__inscription__start_date', distinct=True), Inscription_End=GroupConcat('individual__inscription__end_date', distinct=True), Role=GroupConcat('individual__role__title', distinct=False)).filter(individual__inscription__name__isnull=False).distinct().order_by('name')
#    return render_to_csv_response(InscriptionPeopleSiteDistinct, field_header_map={'site_id': 'Id', 'name': 'name', 'latitude': 'latitude', 'longitude': 'longitude'})

#def Inscriptions_NodesPeopleSitesDistinct(request):
#    InscriptionPeopleSiteDistinct = Site.objects.values('site_id', 'name', 'latitude', 'longitude').annotate(Inscription=GroupConcat('inscription__name', distinct=True), Inscription_Start=GroupConcat('individual__inscription__start_date', distinct=True), Inscription_End=GroupConcat('individual__inscription__end_date', distinct=True)).filter(inscription__name__isnull=False).distinct().order_by('name')
#    return render_to_csv_response(InscriptionPeopleSiteDistinct, field_header_map={'site_id': 'Id', 'name': 'name', 'latitude': 'latitude', 'longitude': 'longitude', 'Inscription': 'inscription', 'Inscription_Start': 'inscription_startdate', 'Inscription_End': 'inscription_enddate'})

#def links(request):
#    return  render(request, 'links.html')
    
def Inscriptions_Nodes(request):
    InscriptionSiteData = Site.objects.values('inscription__inscription_id', 'name', 'latitude', 'longitude', 'inscription__name', 'inscription__start_date', 'inscription__end_date').filter(inscription__name__isnull=False).distinct().order_by('name')
    return render_to_csv_response(InscriptionSiteData, field_header_map={'inscription__inscription_id': 'id', 'name': 'name', 'latitude': 'latitude', 'longitude': 'longitude', 'inscription__name':'inscription', 'inscription__start_date':'start date', 'inscription__end_date':'end date'})

#def Inscriptions_NodesDistinct(request):
#    InscriptionSiteDataDistinct = Site.objects.values('site_id', 'name', 'latitude', 'longitude').filter(inscription__name__isnull=False).annotate(Inscription=GroupConcat('inscription__name', distinct=True), Inscription_Start=GroupConcat('inscription__start_date', distinct=True), Inscription_End=GroupConcat('inscription__end_date', distinct=True), IndividualName=GroupConcat('inscription__individual__name', distinct=True), IndividualRole=GroupConcat('inscription__individual__role__title', distinct=False)).order_by('name')
#    return render_to_csv_response(InscriptionSiteDataDistinct, field_header_map={'site_id': 'Id', 'name': 'name', 'latitude': 'latitude', 'longitude': 'longitude', 'Inscription':'inscription', 'Inscription_Start':'start date', 'Inscription_End':'end date', 'Individual':'individual', 'IndividualName':'name', 'IndividualRole':'role'})

def Inscriptions_NodesPeopleSites(request):
    InscriptionBothSiteData = Site.objects.values('individual__individual_id', 'name', 'latitude', 'longitude', 'individual__name', 'individual__patronym', 'individual__inscription__name', 'individual__inscription__start_date', 'individual__inscription__end_date', 'individual__role__title').filter(individual__inscription__name__isnull=False).distinct().order_by('name')
    return render_to_csv_response(InscriptionBothSiteData, field_header_map={'individual__individual_id': 'id', 'name': 'name', 'latitude': 'latitude', 'longitude': 'longitude', 'individual__inscription__name':'inscription', 'individual__inscription__start_date':'start date', 'individual__inscription__end_date':'end date', 'individual__name':'individual', 'individual__patronym':'individual patronym', 'individual__role__title':'Roles'})

def links(request):
    return  render(request, 'links.html')

def Inscriptions_NodesPeopleSitesDistinct(request):
    InscriptionPeopleSiteDistinct = Site.objects.values('site_id', 'name', 'latitude', 'longitude').annotate(Inscription=GroupConcat('inscription__name', distinct=True), Inscription_Start=GroupConcat('individual__inscription__start_date', distinct=True), Inscription_End=GroupConcat('individual__inscription__end_date', distinct=True)).filter(inscription__name__isnull=False).distinct().order_by('name')
    return render_to_csv_response(InscriptionPeopleSiteDistinct, field_header_map={'site_id': 'Id', 'name': 'name', 'latitude': 'latitude', 'longitude': 'longitude', 'Inscription': 'inscription', 'Inscription_Start': 'inscription_startdate', 'Inscription_End': 'inscription_enddate'})


