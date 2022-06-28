from django_filters import rest_framework as filters
from rest_framework import viewsets

from core.custom_filter import CustomSearchFilter
from core.permissions import IsAdminOrReadOnly
from .models import Dealer, DealerGeneral
from .serializers import DealerSerializer, DealerGeneralSerializer


class DealerFilter(filters.FilterSet):
    name = filters.AllValuesFilter(field_name='name')
    founding_date = filters.DateFromToRangeFilter()
    rating = filters.RangeFilter()
    cars_count = filters.RangeFilter()

    class Meta:
        model = Dealer
        fields = ('name', 'founding_date', 'rating', 'cars_count')


class DealerViewSet(viewsets.ModelViewSet):
    queryset = Dealer.objects.all()
    serializer_class = DealerSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (CustomSearchFilter, filters.DjangoFilterBackend,)
    filterset_class = DealerFilter
    ordering_fields = ('name',)


class DealerGeneralViewSet(viewsets.ModelViewSet):
    queryset = DealerGeneral.objects.all()
    serializer_class = DealerGeneralSerializer
    permission_classes = (IsAdminOrReadOnly,)
