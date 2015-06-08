from samothrace.apps.inscriptions.models import Inscription
from rest_framework import viewsets
from samothrace.apps.inscriptions.serializers import InscriptionSerializer


class InscriptionViewSet(viewsets.ModelViewSet):
    queryset = Inscription.objects.all()
    serializer_class = InscriptionSerializer
