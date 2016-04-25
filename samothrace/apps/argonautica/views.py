from django.shortcuts import render
import csv
from djqscsv import render_to_csv_response
from samothrace.apps.sites.models import Site, Marker, Koina, Ancient_Sources
from samothrace.apps.argonautica.models import Person, Stops, Places_Referenced

from django.conf import settings
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404
from django.db.models import Q
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.template import RequestContext



def Argo_Edges(request):
    ArgoEdgeData = Stops.objects.values('id', 'crew__name', 'crew__origin__site_id', 'crew__origin__name', 'crew__origin__latitude', 'crew__origin__longitude', 'place_of_stop__site_id', 'place_of_stop__name', 'place_of_stop__latitude', 'place_of_stop__longitude').filter(type_of_stop='direct')
    return render_to_csv_response(ArgoEdgeData, field_header_map={'id': 'record_id', 'crew__name': 'crew_member_name', 'crew__origin__site_id': 'source_id', 'crew__origin__name': 'source', 'crew__origin__latitude': 'source_lat', 'crew__origin__longitude': 'source_long', 'place_of_stop__site_id': 'target_id', 'place_of_stop__name': 'target', 'place_of_stop__latitude': 'target_lat', 'place_of_stop__longitude': 'target_long'})


#def map(request):
#    return render(request, 'map.html')
