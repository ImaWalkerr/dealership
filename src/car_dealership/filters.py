from django_filters import rest_framework as filters

from src.car_dealership.models import CarDealerShip, Car


class CarDealerShipFilter(filters.FilterSet):
    name = filters.AllValuesFilter(field_name='name')
    country = filters.AllValuesFilter(field_name='country')
    min_balance = filters.NumberFilter(field_name='balance', lookup_expr='gte')
    max_balance = filters.NumberFilter(field_name='balance', lookup_expr='lte')

    class Meta:
        model = CarDealerShip
        fields = ('name', 'country', 'balance',)


class CarFilter(filters.FilterSet):
    car_model = filters.AllValuesFilter(field_name='car_model')

    class Meta:
        model = Car
        fields = ('car_model',)
