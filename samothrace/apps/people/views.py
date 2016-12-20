from django.shortcuts import render
import csv
from djqscsv import render_to_csv_response
from django.db.models import Q
from samothrace.apps.people.models import Individual, Role, Priesthood
from rest_framework import viewsets
from samothrace.apps.people.serializers import IndividualSerializer, RoleSerializer, PriesthoodSerializer


class IndividualViewSet(viewsets.ModelViewSet):
    queryset = Individual.objects.all()
    serializer_class = IndividualSerializer


class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class PriesthoodViewSet(viewsets.ModelViewSet):
    queryset = Priesthood.objects.all()
    serializer_class = PriesthoodSerializer


def InscriptionPeople_Edges(request):
    PeopleInscriptionEdges = Individual.objects.values('individual_id', 'name', 'site__name', 'name', 'inscription__name', 'inscription__individual__name', 'inscription__individual__site__name').filter(site__name__isnull=False).order_by('inscription__name')
    return render_to_csv_response(PeopleInscriptionEdges, field_header_map={'individual_id': 'id', 'name':'person1', 'site__name':'source', 'inscription__name':'inscription', 'inscription__individual__name':'person2', 'inscription__individual__site__name':'target'})
# Getting there...