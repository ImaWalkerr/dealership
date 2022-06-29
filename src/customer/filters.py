from django_filters import rest_framework as filters

from src.customer.models import Customer


class CustomerFilter(filters.FilterSet):
    first_name = filters.AllValuesFilter(field_name='first_name')
    last_name = filters.AllValuesFilter(field_name='last_name')
    min_balance = filters.NumberFilter(field_name='balance', lookup_expr='gte')
    max_balance = filters.NumberFilter(field_name='balance', lookup_expr='lte')

    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'balance',)
