from django.db import models
from djmoney.models.fields import MoneyField

from core.abstract_field import BaseModel


class Dealer(BaseModel):
    name = models.CharField(max_length=255, verbose_name='Dealer name')
    founding_date = models.CharField(max_length=255, blank=True, verbose_name='Dealer founding date')
    rating = models.PositiveIntegerField(default=None, blank=True, verbose_name='Dealer rating')
    cars_count = models.PositiveIntegerField(default=None, blank=True, verbose_name='Dealer cars')
    customers_count = models.PositiveIntegerField(default=None, blank=True, verbose_name='Dealer customers count')
    car_list_in_sale = models.ManyToManyField(
        to='car_dealership.Car', through='DealerGeneral', verbose_name='Car list in sale',
        related_name='car_list_in_sale'
    )

    def __str__(self):
        return f"{self.name, self.rating}"

    class Meta:
        db_table = 'dealer'
        verbose_name = 'Dealer'
        verbose_name_plural = 'Dealers'
        ordering = ['id']


class DealerGeneral(BaseModel):
    car = models.ForeignKey(
        to='car_dealership.Car', on_delete=models.SET_NULL, null=True, verbose_name='Sold car', related_name='sold_car'
    )
    dealer = models.ForeignKey(
        to=Dealer, on_delete=models.SET_NULL, null=True, verbose_name='Dealership which sold car',
        related_name='dealership_sold_car'
    )
    car_price = MoneyField(
        max_digits=14, decimal_places=2, default_currency='USD', verbose_name='Car price from dealer'
    )
    car_discount = models.PositiveIntegerField(default=None, blank=True, verbose_name='Car discount from dealer')

    def __str__(self):
        return f"{self.car, self.dealer, self.car_price}"

    class Meta:
        db_table = 'dealer_general'
        verbose_name = 'Dealer general'
        verbose_name_plural = 'Dealers general'
        ordering = ['id']
