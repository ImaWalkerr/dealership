from django_filters import rest_framework as filters

from src.dealer.models import Dealer


class DealerFilter(filters.FilterSet):
    name = filters.AllValuesFilter(field_name='name')
    founding_date = filters.DateFromToRangeFilter()
    rating = filters.RangeFilter()
    cars_count = filters.RangeFilter()

    class Meta:
        model = Dealer
        fields = ('name', 'founding_date', 'rating', 'cars_count',)
