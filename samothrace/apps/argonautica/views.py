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
    ArgoEdgeData = Stops.objects.values('id', 'crew__name', 'crew__origin__name', 'place_of_stop__name').filter(type_of_stop='direct')
    return render_to_csv_response(ArgoEdgeData)

