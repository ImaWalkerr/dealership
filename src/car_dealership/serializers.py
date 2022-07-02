from rest_framework import serializers

from src.car_dealership.models import (
    CarDealerShip,
    DealerShipGeneral,
    Car,
)


class CarDealerShipSerializer(serializers.ModelSerializer):
    cars_list = serializers.StringRelatedField(many=True)

    class Meta:
        model = CarDealerShip
        fields = ('name', 'country', 'balance', 'cars_list',)


class DealerShipGeneralSerializer(serializers.ModelSerializer):
    dealership = serializers.RelatedField(read_only=True, allow_null=True)
    car = serializers.RelatedField(read_only=True, allow_null=True)
    customer = serializers.RelatedField(read_only=True, allow_null=True)

    class Meta:
        model = DealerShipGeneral
        fields = ('dealership', 'car', 'customer',)


class CarSerializer(serializers.ModelSerializer):
    car_dealer = serializers.StringRelatedField(many=True)

    class Meta:
        model = Car
        fields = '__all__'
