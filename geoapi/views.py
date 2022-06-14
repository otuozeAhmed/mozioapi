from django.contrib.gis.geos import Point

from .models import GeoLocation, Provider, ServiceArea
from .serializers import LatLngSerializer, ProviderSerializer, ServiceAreaSerializer


from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status



class ProviderView(APIView):
    
    # Read
    def get(self, request, *args, **kwargs):
        '''
        List all providers in a given service area
        '''
        providers = Provider.objects.all()
        serializer = ProviderSerializer(providers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # Post
    def post(self, request, *args, **kwargs):
        '''
        Create a Provider with these basic data
        '''
        data = request.data
        serializer = ProviderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class ProviderDetailView(APIView):
    
    
    def get_object(self, pk):
        '''
        Helper method to get the object with given pk
        '''
        try:
            return Provider.objects.get(id=pk)
        except Provider.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, pk, *args, **kwargs):
        '''
        Retrieves the provider with given provider_id
        '''
        provider_instance = self.get_object(pk)
        if not provider_instance:
            return Response(
                {"res": "Object with provider id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = ProviderSerializer(provider_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, pk, *args, **kwargs):
        '''
        Updates the provider list with given provider_id if exists
        '''
        provider_instance = self.get_object(pk)
        if not provider_instance:
            return Response(
                {"res": "Object with provider id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = request.data
        serializer = ProviderSerializer(instance = provider_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, pk, *args, **kwargs):
        '''
        Deletes the provider data with given provider id if exists
        '''
        provider_instance = self.get_object(pk)
        if not provider_instance:
            return Response(
                {"res": "Object with provider id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        provider_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )


class ServiceAreaView(APIView):
    
    # Read
    def get(self, request, *args, **kwargs):
        '''
        List all service area
        '''
        service_area = ServiceArea.objects.all()
        serializer = ServiceAreaSerializer(service_area, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # Post
    def post(self, request, *args, **kwargs):
        '''
        Creates a service area with these basic data
        '''
        data = request.data
        serializer = ServiceAreaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class ServiceAreaDetailView(APIView):
    
    
    def get_object(self, pk):
        '''
        Helper method to get the object with given pk
        '''
        try:
            return ServiceArea.objects.get(id=pk)
        except ServiceArea.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, pk, *args, **kwargs):
        '''
        Retrieves the service area with given pk
        '''
        service_instance = self.get_object(pk)
        if not service_instance:
            return Response(
                {"res": "Object with service area id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = ServiceAreaSerializer(service_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, pk, *args, **kwargs):
        '''
        Updates the provider list with given pk if exists
        '''
        service_instance = self.get_object(pk)
        if not service_instance:
            return Response(
                {"res": "Object with service area id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = request.data
        serializer = ServiceAreaSerializer(instance = service_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, pk, *args, **kwargs):
        '''
        Deletes the provider data with given service area pk if exists
        '''
        service_instance = self.get_object(pk)
        if not service_instance:
            return Response(
                {"res": "Object with service area id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        service_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )



class LatLngView(APIView):
    '''Returns all the Polygon included in a lat/lng'''
    
    # Read
    def get(self, request, *args, **kwargs):
        '''
        List all providers in a given lat/lng
        '''
        data = GeoLocation.objects.all()
        serializer = LatLngSerializer(data, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    # Post
    def post(self, request, x, y, *args, **kwargs):
        '''
        Create a Polygon with specific lat/lng
        '''
       
        data = GeoLocation.objects.filter(geo__contains=Point(x, y))
        serializer = LatLngSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(
            {"res": "Your point is not avaible in any Polygon in the database"},
            status=status.HTTP_400_BAD_REQUEST)