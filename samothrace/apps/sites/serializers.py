from samothrace.apps.sites.models import Site
from rest_framework import serializers

class SiteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Site
        fields = ('site_id', 'name', 'latitude', 'longitude', 'elevation')
        
