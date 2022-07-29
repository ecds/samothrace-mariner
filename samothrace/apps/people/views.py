from django.shortcuts import render
import csv
from djqscsv import render_to_csv_response
from django.db.models import Q
from samothrace.apps.people.models import Individual, Role, Priesthood
#from rest_framework import viewsets
#from samothrace.apps.people.serializers import IndividualSerializer, RoleSerializer, PriesthoodSerializer


# class IndividualViewSet(viewsets.ModelViewSet):
#     queryset = Individual.objects.all()
#     serializer_class = IndividualSerializer
#
#
# class RoleViewSet(viewsets.ModelViewSet):
#     queryset = Role.objects.all()
#     serializer_class = RoleSerializer
#
#
# class PriesthoodViewSet(viewsets.ModelViewSet):
#     queryset = Priesthood.objects.all()
#     serializer_class = PriesthoodSerializer


#def InscriptionPeople_Edges(request):
#    PeopleInscriptionEdges = Individual.objects.values('individual_id', 'name', 'role__title', 'site__name', 'inscription__name', 'inscription__individual__name', 'inscription__individual__role__title', 'inscription__individual__individual_id', 'inscription__individual__site__name').filter(site__name__isnull=False).order_by('inscription__name')
#    return render_to_csv_response(PeopleInscriptionEdges, field_header_map={'individual_id': 'id', 'name':'person1', 'role__title':'role', 'site__name':'source', 'inscription__name':'inscription', 'inscription__individual__individual_id':'person2_id', 'inscription__individual__name':'person2', 'inscription__individual__role__title':'role2', 'inscription__individual__site__name':'target'})
# Getting there...
def InscriptionPeople_Edges(request):
    PeopleInscriptionEdges = Individual.objects.values('individual_id', 'name', 'site__name', 'inscription__name', 'inscription__individual__name', 'inscription__individual__individual_id', 'inscription__individual__site__name').filter(site__name__isnull=False).order_by('inscription__name')
    return render_to_csv_response(PeopleInscriptionEdges, field_header_map={'individual_id': 'id', 'name':'person1', 'site__name':'source', 'inscription__name':'inscription', 'inscription__individual__individual_id':'person2_id', 'inscription__individual__name':'person2', 'inscription__individual__site__name':'target'})

def Bibliography(request):
    return  render(request, 'biblio.html')

def HowToGraph(request):
    return  render(request, 'how_graph.html')

def InscriptionPeopleTime_Edges(request):
    PeopleInscriptionEdgesTime = Individual.objects.values('individual_id', 'name', 'role__title', 'site__name', 'inscription__name', 'inscription__individual__name', 'inscription__individual__role__title', 'inscription__individual__individual_id', 'inscription__individual__site__name', 'inscription__start_date', 'inscription__end_date').filter(site__name__isnull=False).order_by('inscription__name')
    return render_to_csv_response(PeopleInscriptionEdgesTime, field_header_map={'individual_id': 'id', 'name':'person1', 'role__title':'role', 'site__name':'head', 'inscription__name':'inscription', 'inscription__individual__individual_id':'person2_id', 'inscription__individual__name':'person2', 'inscription__individual__role__title':'role2', 'inscription__individual__site__name':'tail', 'inscription__start_date':'onset',  'inscription__end_date':'terminus'})
# Getting with time data...
