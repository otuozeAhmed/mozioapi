from django.urls import path, register_converter

from .views import (LatLngView, 
                    ProviderDetailView, 
                    ProviderView, 
                    ServiceAreaDetailView, 
                    ServiceAreaView)

from .converters import FloatUrlParameterConverter



register_converter(FloatUrlParameterConverter, 'float')

urlpatterns = [
    path('providers/', ProviderView.as_view(), name='providers'),
    path('service-area/', ServiceAreaView.as_view(), name='service-area'),
    path('lat-lng/<float:x>/<float:y>/', LatLngView.as_view()),
    path('providers/<int:pk>/', ProviderDetailView.as_view(), name='provider_detail'),
    path('service-area/<int:pk>/', ServiceAreaDetailView.as_view(), name='service-area-detail'), 
    
]