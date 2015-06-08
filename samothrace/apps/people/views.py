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
