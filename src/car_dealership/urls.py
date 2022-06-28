from django.urls import path, include
from .views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'dealership', CarDealerShipViewSet, basename='dealership')
router.register(r'dealership_general', DealerShipGeneralViewSet, basename='dealership_general')
router.register(r'cars', CarViewSet, basename='cars')
router.register(r'cars_info', CarInfoViewSet, basename='cars_info')

urlpatterns = [
    path('dealership/', include(router.urls)),
]
