from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from .models import GeoLocation, Provider, ServiceArea

class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = '__all__'
        
    
class ServiceAreaSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = ServiceArea
        geo_field = 'geom'
        fields = '__all__'
        
        
class LatLngSerializer(GeoFeatureModelSerializer):
    
    provider__name = serializers.CharField(source='provider.name', read_only=True)
    polygon_name = serializers.CharField(source='service_area.name', read_only=True)
    price = serializers.CharField(source='service_area.price', read_only=True)
    
    class Meta:
        model = GeoLocation
        geo_field = 'geo'
        fields = ('provider__name', 'polygon_name', 'price',)
        
    
