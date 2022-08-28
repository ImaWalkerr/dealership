from rest_framework import serializers

from src.car_dealership.models import (
    CarDealerShip,
    DealerShipGeneral,
    Car,
)


class CarDealerShipSerializer(serializers.ModelSerializer):
    cars_list = serializers.StringRelatedField()

    class Meta:
        model = CarDealerShip
        fields = ('name', 'country', 'balance', 'cars_list',)


class DealerShipGeneralSerializer(serializers.ModelSerializer):
    dealership = serializers.StringRelatedField()
    car = serializers.StringRelatedField()
    customer = serializers.StringRelatedField()

    class Meta:
        model = DealerShipGeneral
        fields = ('dealership', 'car', 'customer',)


class CarSerializer(serializers.ModelSerializer):
    car_dealer = serializers.StringRelatedField()

    class Meta:
        model = Car
        fields = '__all__'
