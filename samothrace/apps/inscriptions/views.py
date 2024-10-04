from django.shortcuts import render
import csv
from djqscsv import render_to_csv_response
from django.db.models import Q
from samothrace.apps.inscriptions.models import Inscription, Grant
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


def Grant_Edges1(request):
    GrantEdgesGrant = Grant.objects.values('id', 'inscription', 'granting_name__name', 'receiving_name__name').filter(granting_name__name__isnull=False).order_by('inscription')
    return render_to_csv_response(GrantEdgesGrant, field_header_map={'inscription':'inscription', 'granting_name__name':'source', 'receiving_name__name':'target'})
# Starburst

#def Grant_Edges2(request):
#    GrantEdgesRec = Grant.objects.values('id', 'inscription', 'granting_name__receiving_name__name', 'receiving_name__name').order_by('inscription')
#    return render_to_csv_response(GrantEdgesRec, field_header_map={'inscription':'inscription', 'granting_name__name__receiving_name__name':'source', 'receiving_name__name':'target'})
# Not Getting there...


def Grant_Edges4(request):
    GrantEdgesReceivings = Grant.objects.values('id', 'inscription', 'receiving_name__name', 'site__receiving_name__name').filter(receiving_name__name__isnull=False).order_by('inscription')
    return render_to_csv_response(GrantEdgesReceivings, field_header_map={'inscription':'inscription', 'receiving_name__name':'source', 'site__receiving_name__name':'target'})
# Starburst