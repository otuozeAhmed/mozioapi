from django.contrib import admin
from django.contrib.gis import admin

from .models import GeoLocation, Provider, ServiceArea


@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'language',)
    

@admin.register(ServiceArea)
class ServiceAreaAdmin(admin.OSMGeoAdmin):
    list_display = ('name', 'price', 'geom',)
    

@admin.register(GeoLocation)
class GeoLocationAdmin(admin.OSMGeoAdmin):
    list_display = ('geo',)
    
    

