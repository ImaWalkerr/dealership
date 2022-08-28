from rest_framework import serializers

from src.dealer.models import Dealer, DealerGeneral


class DealerSerializer(serializers.ModelSerializer):
    customers_count = serializers.StringRelatedField()
    car_list_in_sale = serializers.StringRelatedField()

    class Meta:
        model = Dealer
        fields = ('name', 'founding_date', 'rating', 'cars_count', 'customers_count', 'car_list_in_sale',)


class DealerGeneralSerializer(serializers.ModelSerializer):
    car = serializers.StringRelatedField()
    dealer = serializers.StringRelatedField()

    class Meta:
        model = DealerGeneral
        fields = ('car', 'dealer', 'car_price', 'car_discount',)
