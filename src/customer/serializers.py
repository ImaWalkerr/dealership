from rest_framework import serializers

from customer.models import *


class CustomerSerializer(serializers.ModelSerializer):
    purchase_history = serializers.RelatedField(read_only=True, allow_null=True)

    class Meta:
        model = Customer
        fields = ['balance', 'birthday', 'purchase_history']


class CustomerCarSerializer(serializers.ModelSerializer):
    customer = serializers.RelatedField(read_only=True, allow_null=True)
    car = serializers.RelatedField(read_only=True, allow_null=True)
    car_dealership = serializers.RelatedField(read_only=True, allow_null=True)

    class Meta:
        model = CustomerCar
        fields = ['customer', 'car', 'car_features', 'car_dealership', 'discount', 'price']
