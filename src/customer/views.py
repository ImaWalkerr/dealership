from django_filters import rest_framework as filters
from rest_framework import viewsets

from core.permissions import IsAdminOrReadOnly
from customer.filters import CustomerFilter
from src.customer.models import Customer, CustomerCar
from src.customer.serializers import CustomerSerializer, CustomerCarSerializer


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
