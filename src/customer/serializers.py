from rest_framework import serializers

from src.customer.models import Customer, CustomerCar


class CustomerSerializer(serializers.ModelSerializer):
    purchase_history = serializers.StringRelatedField()
    car_features = serializers.JSONField()

    class Meta:
        model = Customer
        fields = ('id', 'first_name', 'last_name', 'email', 'balance', 'birthday', 'purchase_history', 'car_features')


class CustomerCarSerializer(serializers.ModelSerializer):
    customer = serializers.StringRelatedField()
    car = serializers.StringRelatedField()
    car_dealership = serializers.StringRelatedField()

    class Meta:
        model = CustomerCar
        fields = ('customer', 'car', 'car_dealership', 'discount', 'price',)
