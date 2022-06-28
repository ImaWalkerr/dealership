from django_filters import rest_framework as filters
from rest_framework import viewsets

from core.permissions import IsAdminOrReadOnly
from .models import Customer, CustomerCar
from .serializers import CustomerSerializer, CustomerCarSerializer


class CustomerFilter(filters.FilterSet):
    first_name = filters.AllValuesFilter(field_name='first_name')
    last_name = filters.AllValuesFilter(field_name='last_name')
    min_balance = filters.NumberFilter(field_name='balance', lookup_expr='gte')
    max_balance = filters.NumberFilter(field_name='balance', lookup_expr='lte')

    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'balance')


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CustomerFilter
    ordering_fields = ('last_name',)


class CustomerCarViewSet(viewsets.ModelViewSet):
    queryset = CustomerCar.objects.all()
    serializer_class = CustomerCarSerializer
    permission_classes = (IsAdminOrReadOnly,)
