import json

from django.test import TestCase
from django.urls import reverse
from django.contrib.gis.geos import Polygon

from geoapi.serializers import ProviderSerializer, ServiceAreaSerializer
from rest_framework import status

from .models import Provider, ServiceArea


class GetAllProviders(TestCase):
    """ Test module for GET all providers API """
    
    def setUp(self):
        
        Provider.objects.create(
            name='Justin', 
            email='justin@email.com', 
            phone_number=+2348164646329, 
            language='English', 
            currency='USD')
        
        Provider.objects.create(
            name='John', 
            email='John@email.com', 
            phone_number=+2347018425958, 
            language='French', 
            currency='AUD')
        
    def test_get_all_providers(self):
        # get API response
        response = self.client.get(reverse('providers'))
        
        # get data from db
        providers = Provider.objects.all()
        serializer = ProviderSerializer(providers, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        

class GetSingleProviderTest(TestCase):
    """ Test module for GET single provider API """

    def setUp(self):
        
        self.provider = Provider.objects.create(
            name='Justin', 
            email='justin@email.com', 
            phone_number=+2348164646329, 
            language='English', 
            currency='USD')
        
        self.provider2 = Provider.objects.create(
            name='John', 
            email='John@email.com', 
            phone_number=+2347018425958, 
            language='French', 
            currency='AUD')
       
    def test_get_valid_single_provider(self):
        response = self.client.get(
            reverse('provider_detail', kwargs={'pk': self.provider.pk}))
        provider = Provider.objects.get(pk=self.provider.pk)
        serializer = ProviderSerializer(provider)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_provider(self):
        response = self.client.get(
            reverse('provider_detail', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    
class CreateNewProviderTest(TestCase):
    """ Test module for inserting a new provider """

    def setUp(self):
        self.valid_payload = {
            "id": 1,
            "name": "Ahmedrufai Otuoze",
            "email": "otuozeahmedrufai@gmail.com",
            "phone_number": "+2348164646329",
            "language": "English",
            "currency": "Great Britain Pound"
        }
        self.invalid_payload = {
            "name": 4, 
            "email":"rufai@email.com", 
            "phone_number":"name", 
            "language":"French", 
            "currency":"USD"
        }

    def test_create_valid_provider(self):
        response = self.client.post(
            reverse('providers'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_provider(self):
        response = self.client.post(
            reverse('providers'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
        
class UpdateSingleProviderTest(TestCase):
    """ Test module for updating an existing provider record """

    def setUp(self):
        self.provider = Provider.objects.create(
            name='Ahmedrufai Otuoze', 
            email='otuozeahmedrufai@gmail.com', 
            phone_number=+2348164646329, 
            language='English', 
            currency='Great Britain Pound')
        
        Provider.objects.create(
            name='John', 
            email='John@email.com', 
            phone_number=+2347018425958, 
            language='French', 
            currency='AUD')
        
        self.valid_payload = {
            "id": 1,
            "name": "Ahmedrufai Otuoze",
            "email": "otuozeahmedrufai@gmail.com",
            "phone_number": "+2348164646329",
            "language": "English",
            "currency": "Great Britain Pound"
        }
        self.invalid_payload = {
            "name": 4, 
            "email":"rufai@email.com", 
            "phone_number":"name", 
            "language":"French", 
            "currency":"USD"
        }

    def test_valid_update_provider(self):
        response = self.client.put(
            reverse('provider_detail', kwargs={'pk': self.provider.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_provider(self):
        response = self.client.put(
            reverse('provider_detail', kwargs={'pk': self.provider.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
        

class GetAllServiceArea(TestCase):
    """ Test module for GET all service area API """
    
    def setUp(self):
        self.provider = Provider.objects.create(
            name='Justin', 
            email='justin@email.com', 
            phone_number=+2348164646329, 
            language='English', 
            currency='USD')
        
        ServiceArea.objects.create(
            provider=self.provider,
            name="Rufai",
            price=433,
            geom=(
                Polygon(((0.0, 0.0), (0.0, 50.0), (50.0, 50.0), (50.0, 0.0), (0.0, 0.0)))
            )
        )
        
        
    def test_get_all_service_area(self):
        # get API response
        response = self.client.get(reverse('service-area'))
        
        # get data from db
        service_area = ServiceArea.objects.all()
        serializer = ServiceAreaSerializer(service_area, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        

class GetSingleServiceAreaTest(TestCase):
    """ Test module for GET single service area API """

    def setUp(self):
        
        self.provider = Provider.objects.create(
            name='Justin', 
            email='justin@email.com', 
            phone_number=+2348164646329, 
            language='English', 
            currency='USD')
        
        self.service_area = ServiceArea.objects.create(
            provider=self.provider,
            name="Rufai",
            price=433,
            geom=(
                Polygon(((0.0, 0.0), (0.0, 50.0), (50.0, 50.0), (50.0, 0.0), (0.0, 0.0)))
            )
        )
        
        self.service_area_2 = ServiceArea.objects.create(
            provider=self.provider,
            name="Rufai",
            price=433,
            geom=(
                Polygon(((0.0, 0.0), (0.0, 50.0), (50.0, 50.0), (50.0, 0.0), (0.0, 0.0)))
            )
        )
       
    def test_get_valid_single_service_area(self):
        response = self.client.get(
            reverse('service-area-detail', kwargs={'pk': self.service_area.pk}))
        service_area = ServiceArea.objects.get(pk=self.service_area.pk)
        serializer = ServiceAreaSerializer(service_area)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_service_area(self):
        response = self.client.get(
            reverse('service-area-detail', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
        
