from django.contrib.auth.models import AbstractUser
from django.db import models
from djmoney.models.fields import MoneyField
from djmoney.models.validators import MinMoneyValidator

from core.abstract_field import BaseModel


class Customer(AbstractUser):
    balance = models.DecimalField(
        default=None, null=True, blank=True, max_digits=14, decimal_places=2, verbose_name='Customer balance'
    )
    birthday = models.DateField(default=None, null=True, blank=True, verbose_name='Customer birthday')
    purchase_history = models.ManyToManyField(
        'CustomerHistory', verbose_name='Purchase history', related_name='purchase_history'
    )

    def __str__(self):
        return f"{self.first_name, self.last_name, self.balance}"

    class Meta:
        db_table = 'customer'
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'


class CustomerHistory(BaseModel):
    dealership = models.ForeignKey(
        to='car_dealership.CarDealerShip', on_delete=models.CASCADE, verbose_name='Dealership name',
        related_name='dealership_name'
    )
    bayed_cars = models.ManyToManyField(to='car_dealership.Car', verbose_name='Bayed cars', related_name='bayed_cars')

    def __str__(self):
        return f"{self.dealership, self.bayed_cars}"

    class Meta:
        db_table = 'customer_history'
        verbose_name = 'Customer History'
        verbose_name_plural = 'Customers History'


class Offer(BaseModel):
    customer = models.ForeignKey(
        to='customer.Customer', on_delete=models.CASCADE, verbose_name='Customer', related_name='customer_offer'
    )
    car = models.ForeignKey(
        to='car_dealership.Car', on_delete=models.CASCADE, verbose_name='Car for action', related_name='car_for_action'
    )
    car_info = models.JSONField()
    car_dealership = models.ForeignKey(
        to='car_dealership.CarDealerShip', on_delete=models.CASCADE, verbose_name='Car Dealership action',
        related_name='car_dealership_action'
    )
    action_name = models.CharField(max_length=255, verbose_name='Action name')
    action_info = models.TextField(max_length=5000, verbose_name='Action description')
    discount = models.PositiveIntegerField(default=None, blank=True, null=True, verbose_name='Action discount for car')
    price = MoneyField(
        max_digits=14, decimal_places=2, default_currency='USD', validators=[MinMoneyValidator(500)],
        verbose_name='Car price from customer'
    )

    def __str__(self):
        return f"{self.customer, self.car}"

    class Meta:
        db_table = 'customer_offer'
        verbose_name = 'Customer Offer'
        verbose_name_plural = 'Customers Offers'
