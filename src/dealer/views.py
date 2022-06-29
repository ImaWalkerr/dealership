from django_filters import rest_framework as filters
from rest_framework import viewsets

from core.custom_filter import CustomSearchFilter
from core.permissions import IsAdminOrReadOnly
from src.dealer.filters import DealerFilter
from src.dealer.models import Dealer, DealerGeneral
from src.dealer.serializers import DealerSerializer, DealerGeneralSerializer


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
