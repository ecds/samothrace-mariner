from samothrace.apps.people.models import Individual, Role, Priesthood
from rest_framework import serializers

class IndividualSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Individual
        fields = ('individual_id', 'name', 'patronym', 'inscription', 'site', 'comments', 'site_origin')


class RoleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Role
        fields = ('role_id', 'individual', 'title', 'certainty', 'comments')

    
class PriesthoodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Priesthood
        fields = ('priesthood_id', 'name', 'title', 'inscription', 'location', 'deity_id', 'deity', 'duration', 'att_honor', 'cer_ritual', 'comments', 'role')
