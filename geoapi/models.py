from django.db import models
from django.contrib.gis.db import models as gis_models
from django.core.validators import RegexValidator
from django.urls import reverse


class Provider(models.Model):
    """Provider API Model"""
    
    CURRENCY_CHOICES = (
        ('US Dollars', 'USD'),
        ('Australia Dollar', 'AUD'),
        ('Great Britain Pound', 'GBP'),
        ('Bitcoin', 'BTC'),
        ('Nigerian Naira', 'NGN'),
    )
    
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=254, null=True, blank=True)
    email = models.EmailField(max_length=254,null=True, blank=True, unique=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', 
                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], 
                                    max_length=17, blank=True)
    language = models.CharField(max_length=254, null=True, blank=True, 
                                help_text='Language preferred by the vendor')
    currency = models.CharField(max_length=254, default='USD', choices=CURRENCY_CHOICES)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("provider_detail", args=[str(self.pk)])
    

class ServiceArea(models.Model):
    """Service Area API model"""
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=254, null=True, blank=True)
    price = models.DecimalField(max_digits=14, decimal_places=2, null=True, blank=True)
    geom = gis_models.PolygonField(srid=4326, null=True, blank=True)
    
    def __str__(self):
        return self.name

    
class GeoLocation(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, null=True, blank=True)
    service_area = models.ForeignKey(ServiceArea, on_delete=models.CASCADE, null=True, blank=True)
    geo = gis_models.PolygonField(srid=4326, null=True, blank=True)

    def __str__(self):
        return self.provider.name
    