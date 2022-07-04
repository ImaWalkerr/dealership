from django.urls import path, include
from src.car_dealership.views import (
    CarDealerShipViewSet,
    DealerShipGeneralViewSet,
    CarViewSet,
)
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'dealership', CarDealerShipViewSet, basename='dealership')
router.register(r'dealership_general', DealerShipGeneralViewSet, basename='dealership_general')
router.register(r'cars', CarViewSet, basename='cars')

urlpatterns = [
    path('dealership/', include(router.urls)),
]
