from samothrace.apps.sites.models import Site, Marker, Koina
from rest_framework import serializers

class SiteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Site
        fields = ('site_id', 'name', 'mod_name', 'alt_name', 'latitude', 'longitude', 'elevation', 'pleiades_url', 'perseus_url', 'caption', 'paragraph')


class MarkerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Marker
        fields = ('marker_id', 'site', 'type',)


class KoinaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Koina
        fields = ('koina_id', 'site', 'inscription', 'member_count', 'activities', 'comments')
        
