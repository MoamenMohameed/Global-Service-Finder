from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework import serializers
from .models import Services

class ServicesSerializer(GeoFeatureModelSerializer):
    
    distance = serializers.SerializerMethodField()

    class Meta:
        model = Services
        geo_field = "service_location"  
        fields = ('id', 'service', 'service_type', 'distance')

    def get_distance(self, obj):
        if hasattr(obj, 'distance') and obj.distance is not None:
            return obj.distance.m 
        return None