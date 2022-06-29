from django_filters import rest_framework as filters
from rest_framework import viewsets

from src.car_dealership.filters import CarDealerShipFilter, CarFilter
from core.custom_filter import CustomSearchFilter
from core.permissions import IsAdminOrReadOnly
from src.car_dealership.models import Car, CarInfo
from src.car_dealership.serializers import (
    CarDealerShip,
    CarDealerShipSerializer,
    DealerShipGeneral,
    DealerShipGeneralSerializer,
    CarSerializer,
    CarInfoSerializer
)


class CarDealerShipViewSet(viewsets.ModelViewSet):
    queryset = CarDealerShip.objects.all()
    serializer_class = CarDealerShipSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (CustomSearchFilter, filters.DjangoFilterBackend,)
    filterset_class = CarDealerShipFilter
    ordering_fields = ('name',)


class DealerShipGeneralViewSet(viewsets.ModelViewSet):
    queryset = DealerShipGeneral.objects.all()
    serializer_class = DealerShipGeneralSerializer
    permission_classes = (IsAdminOrReadOnly,)


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CarFilter
    ordering_fields = ('car_model',)


class CarInfoViewSet(viewsets.ModelViewSet):
    queryset = CarInfo.objects.all()
    serializer_class = CarInfoSerializer
    permission_classes = (IsAdminOrReadOnly,)
    ordering_fields = ('car_brand',)
