from django.shortcuts import render
import csv
from djqscsv import render_to_csv_response
from django.db.models import Q
from samothrace.apps.inscriptions.models import Inscription
from rest_framework import viewsets
from samothrace.apps.inscriptions.serializers import InscriptionSerializer


class InscriptionViewSet(viewsets.ModelViewSet):
    queryset = Inscription.objects.all()
    serializer_class = InscriptionSerializer


    
#working - edges
def Inscriptions_Edges(request):
    InscriptionEdgeData = Inscription.objects.values('find_spot__site_id', 'find_spot__name', 'name', 'individual__name', 'individual__site__name').filter(name__isnull=False, individual__site__name__isnull=False).distinct().order_by('name')
    return render_to_csv_response(InscriptionEdgeData, field_header_map={'find_spot__site_id': 'Id', 'find_spot__name': 'source', 'name':'inscription', 'individual__name':'individual', 'individual__site__name':'target'})
# Findspot to each person city...
# Something is wrong! Okay - Findspot wrong...


def Inscriptions_Edges2(request):
    InscriptionEdgesData = Inscription.objects.values('inscription_id', 'individual__name', 'individual__site_origin__name', 'name', 'individual__name', 'individual__site_origin__name').filter(name__isnull=False, individual__site_origin__name__isnull=False).distinct().order_by('name')
    return render_to_csv_response(InscriptionEdgesData, field_header_map={'inscription_id': 'id', 'individual__name':'person1', 'individual__site_origin__name':'source', 'name':'inscription', 'individual__name':'individual2', 'individual__site_origin__name':'target'})
# Also doesn't work - just repeats two of individual2 and target