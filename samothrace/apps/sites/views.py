from django.shortcuts import render
import csv
from djqscsv import render_to_csv_response
from django.db.models import Q
from samothrace.apps.sites.models import Site, Marker, Koina
#from rest_framework import viewsets
#from samothrace.apps.sites.serializers import SiteSerializer, MarkerSerializer, KoinaSerializer
from samothrace.apps.sites.models import Site, Marker, Koina, Ancient_Sources
from samothrace.apps.argonautica.models import Person, Stops, Places_Referenced
from samothrace.apps.people.models import Individual, Role, Priesthood
from samothrace.apps.inscriptions.models import Inscription, Grant
#from django_mysql.models import GroupConcat

# class SiteViewSet(viewsets.ModelViewSet):
#     queryset = Site.objects.all()
#     serializer_class = SiteSerializer
#
#
# class MarkerViewSet(viewsets.ModelViewSet):
#     queryset = Marker.objects.all()
#     serializer_class = MarkerSerializer
#
#
# class KoinaViewSet(viewsets.ModelViewSet):
#     queryset = Koina.objects.all()
#     serializer_class = KoinaSerializer

def Inscriptions_Nodes(request):
    InscriptionSiteData = Site.objects.values('inscription__inscription_id', 'name', 'latitude', 'longitude', 'inscription__name', 'inscription__start_date', 'inscription__end_date').filter(inscription__name__isnull=False).distinct().order_by('name')
    return render_to_csv_response(InscriptionSiteData, field_header_map={'inscription__inscription_id': 'name', 'name': 'id', 'latitude': 'latitude', 'longitude': 'longitude', 'inscription__name':'inscription', 'inscription__start_date':'start date', 'inscription__end_date':'end date'})

#def Inscriptions_NodesDistinct(request):
#    InscriptionSiteDataDistinct = Site.objects.values('site_id', 'name', 'latitude', 'longitude').filter(inscription__name__isnull=False).annotate(Inscription=GroupConcat('inscription__name', distinct=True), Inscription_Start=GroupConcat('inscription__start_date', distinct=True), Inscription_End=GroupConcat('inscription__end_date', distinct=True), Individual=GroupConcat('inscription__individual__individual_id', distinct=True), IndividualName=GroupConcat('inscription__individual__name', distinct=True), IndividualRole=GroupConcat('inscription__individual__role__title', distinct=False)).order_by('name')
#    return render_to_csv_response(InscriptionSiteDataDistinct, field_header_map={'site_id': 'Id', 'name': 'name', 'latitude': 'latitude', 'longitude': 'longitude', 'Inscription':'inscription', 'Inscription_Start':'start date', 'Inscription_End':'end date', 'Individual':'individual', 'IndividualName':'name', 'IndividualRole':'role'})

def Inscriptions_NodesPeopleSites(request):
    InscriptionBothSiteData = Site.objects.values('individual__individual_id', 'name', 'latitude', 'longitude', 'individual__name', 'individual__patronym', 'individual__inscription__name', 'individual__inscription__start_date', 'individual__inscription__end_date', 'individual__role__title').filter(individual__inscription__name__isnull=False).distinct().order_by('name')
    return render_to_csv_response(InscriptionBothSiteData, field_header_map={'individual__individual_id': 'name', 'name': 'id', 'latitude': 'latitude', 'longitude': 'longitude', 'individual__inscription__name':'inscription', 'individual__inscription__start_date':'start date', 'individual__inscription__end_date':'end date', 'individual__name':'individual', 'individual__patronym':'individual patronym', 'individual__role__title':'Roles'})

def links(request):
    return  render(request, 'links.html')

def Inscriptions_NodesPeopleSitesDistinct(request):
    InscriptionPeopleSiteDistinct = Site.objects.values('site_id', 'name', 'latitude', 'longitude').annotate(Inscription=GroupConcat('inscription__name', distinct=True), Inscription_Start=GroupConcat('individual__inscription__start_date', distinct=True), Inscription_End=GroupConcat('individual__inscription__end_date', distinct=True)).filter(inscription__name__isnull=False).distinct().order_by('name')
    return render_to_csv_response(InscriptionPeopleSiteDistinct, field_header_map={'site_id': 'Id', 'name': 'name', 'latitude': 'latitude', 'longitude': 'longitude', 'Inscription': 'inscription', 'Inscription_Start': 'inscription_startdate', 'Inscription_End': 'inscription_enddate'})

def Grant_Edges2(request):
    GrantEdgesRec = Site.objects.values('receiving__id', 'name', 'receiving__inscription', 'receiving__granting_name__granting__receiving_name__name').filter(receiving__id__isnull=False).order_by('receiving__inscription')
    return render_to_csv_response(GrantEdgesRec, field_header_map={'name':'source', 'receiving__inscription':'inscription', 'receiving__granting_name__granting__receiving_name__name':'target'})
# maybe... Receiving network without direct granting connections.

def Grant_Edges3(request):
    GrantEdgesOther = Site.objects.values('name', 'granting__inscription', 'granting__receiving_name__name').filter(granting__id__isnull=False).order_by('granting__inscription')
    return render_to_csv_response(GrantEdgesOther, field_header_map={'name':'source', 'granting__inscription':'inscription', 'granting__receiving_name__name':'target'})
# Getting there... starburst - eg. granting edges to receiving nodes

def Grant_Nodes1(request):
    GrantNodesGranting = Site.objects.values('name', 'latitude', 'longitude', 'batlas', 'pleiades_url', 'perseus_url', 'caption', 'paragraph').filter(granting__id__isnull=False).distinct().order_by('name')
    return render_to_csv_response(GrantNodesGranting, field_header_map={'name':'id'})

def Grant_Nodes2(request):
    GrantNodesReceiving = Site.objects.values('name', 'latitude', 'longitude', 'batlas', 'pleiades_url', 'perseus_url', 'caption', 'paragraph').filter(receiving__id__isnull=False).distinct().order_by('name')
    return render_to_csv_response(GrantNodesReceiving, field_header_map={'name':'id'})
