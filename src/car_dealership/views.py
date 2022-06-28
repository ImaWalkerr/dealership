from django_filters import rest_framework as filters
from rest_framework import viewsets

from core.custom_filter import CustomSearchFilter
from core.permissions import IsAdminOrReadOnly
from .serializers import *


class CarDealerShipFilter(filters.FilterSet):
    name = filters.AllValuesFilter(field_name='name')
    country = filters.AllValuesFilter(field_name='country')
    min_balance = filters.NumberFilter(field_name='balance', lookup_expr='gte')
    max_balance = filters.NumberFilter(field_name='balance', lookup_expr='lte')

    class Meta:
        model = CarDealerShip
        fields = ['name', 'country', 'balance']


class CarDealerShipViewSet(viewsets.ModelViewSet):
    queryset = CarDealerShip.objects.all()
    serializer_class = CarDealerShipSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (CustomSearchFilter, filters.DjangoFilterBackend,)
    filterset_class = CarDealerShipFilter
    ordering_fields = ['name']


class DealerShipGeneralViewSet(viewsets.ModelViewSet):
    queryset = DealerShipGeneral.objects.all()
    serializer_class = DealerShipGeneralSerializer
    permission_classes = (IsAdminOrReadOnly,)


class CarFilter(filters.FilterSet):
    car_model = filters.AllValuesFilter(field_name='car_model')

    class Meta:
        model = Car
        fields = ['car_model']


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CarFilter
    ordering_fields = ['car_model']


class CarInfoViewSet(viewsets.ModelViewSet):
    queryset = CarInfo.objects.all()
    serializer_class = CarInfoSerializer
    permission_classes = (IsAdminOrReadOnly,)
    ordering_fields = ['car_brand']
