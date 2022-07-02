from django.contrib.auth.models import AbstractUser
from django.db import models
from djmoney.models.fields import MoneyField
from djmoney.models.validators import MinMoneyValidator

from core.abstract_field import BaseModel


def get_default_features():
    return {
        'car_model': 'BMW',
        'car_year': 2000,
        'car_color': 'YELLOW',
        'car_interior_color': 'BROWN',
        'car_mileage': 100000,
        'car_body_type': 'SEDAN',
        'car_engine_type': 'INLINE',
        'car_engine_volume': 5.5,
        'car_gearbox': 'AUTOMATIC',
        'number_of_doors': 4,
        'VIN': '1HGBH41JXMN109186',
        'electric_car': True,
    }


class Customer(AbstractUser):
    balance = models.DecimalField(
        default=None, null=True, blank=True, max_digits=14, decimal_places=2, verbose_name='Customer balance'
    )
    birthday = models.DateField(default=None, null=True, blank=True, verbose_name='Customer birthday')
    purchase_history = models.ForeignKey(
        'CustomerCar', on_delete=models.SET_NULL, null=True, verbose_name='Customer offer',
        related_name='customer_offer'
    )
    car_features = models.JSONField(
        encoder=None,
        decoder=None,
        blank=True,
        default=get_default_features,
        verbose_name='Car features',
    )

    def __str__(self):
        return f"{self.first_name, self.last_name, self.balance}"

    class Meta:
        db_table = 'customer'
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
        ordering = ['id']


class CustomerCar(BaseModel):
    customer = models.ForeignKey(
        to='customer.Customer', on_delete=models.SET_NULL, null=True, verbose_name='Customer',
        related_name='customer'
    )
    car = models.ForeignKey(
        to='car_dealership.Car', on_delete=models.SET_NULL, null=True, verbose_name='Car for action',
        related_name='car'
    )
    car_dealership = models.ForeignKey(
        to='car_dealership.CarDealerShip', on_delete=models.SET_NULL, null=True, verbose_name='Car Dealership action',
        related_name='car_dealership'
    )
    discount = models.PositiveIntegerField(default=None, blank=True, null=True, verbose_name='Action discount for car')
    price = MoneyField(
        max_digits=14, decimal_places=2, default_currency='USD', validators=[MinMoneyValidator(500)],
        verbose_name='Car price from customer'
    )

    def __str__(self):
        return f"{self.customer, self.car, self.price}"

    class Meta:
        db_table = 'customer_offer'
        verbose_name = 'Customer Offer'
        verbose_name_plural = 'Customers Offers'
        ordering = ['id']
