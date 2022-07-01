from rest_framework import serializers

from src.customer.models import Customer, CustomerCar


class CustomerSerializer(serializers.ModelSerializer):
    purchase_history = serializers.RelatedField(read_only=True, allow_null=True)
    car_features = serializers.JSONField()

    class Meta:
        model = Customer
        fields = ('id', 'first_name', 'last_name', 'email', 'balance', 'birthday', 'purchase_history', 'car_features')


class CustomerCarSerializer(serializers.ModelSerializer):
    customer = serializers.RelatedField(read_only=True, allow_null=True)
    car = serializers.RelatedField(read_only=True, allow_null=True)
    car_dealership = serializers.RelatedField(read_only=True, allow_null=True)

    class Meta:
        model = CustomerCar
        fields = ('customer', 'car', 'car_dealership', 'discount', 'price',)
