from rest_framework import serializers

from src.car_dealership.models import (
    CarDealerShip,
    DealerShipGeneral,
    Car,
    CarInfo
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


class CarInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarInfo
        fields = '__all__'


class CarSerializer(serializers.ModelSerializer):
    car_info = CarInfoSerializer(many=True, read_only=True)
    car_dealer = serializers.StringRelatedField(many=True)

    class Meta:
        model = Car
        fields = ('car_model', 'car_info', 'car_dealer',)
