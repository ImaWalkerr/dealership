from django.db import models
from djmoney.models.fields import MoneyField

from core.abstract_field import BaseModel


class Dealer(BaseModel):
    name = models.CharField(max_length=255, verbose_name='Dealer name')
    founding_date = models.DateField(default=None, blank=True, verbose_name='Dealer founding date')
    rating = models.IntegerField(default=None, blank=True, verbose_name='Dealer rating')
    customers_count = models.ManyToManyField(
        to='customer.Customer', verbose_name='Customers count', related_name='customers_count'
    )
    car_list_in_sale = models.ManyToManyField(
        to='car_dealership.Car', verbose_name='Car list in sale', related_name='car_list_in_sale'
    )
    dealer_price = models.ManyToManyField(
        'DealerPrice', verbose_name='Dealer price for cars', related_name='dealer_price_for_cars'
    )
    dealer_sales_history = models.ManyToManyField(
        'DealerSalesHistory', verbose_name='Dealer sales history', related_name='dealer_sales_history'
    )

    def __str__(self):
        return f"{self.name, self.rating}"

    class Meta:
        db_table = 'dealer'
        verbose_name = 'Dealer'
        verbose_name_plural = 'Dealers'


class DealerPrice(BaseModel):
    car_price = MoneyField(
        max_digits=14, decimal_places=2, default_currency='USD', verbose_name='Car price from dealer'
    )
    car_discount = models.PositiveIntegerField(default=None, blank=True, verbose_name='Car discount from dealer')
    car_model = models.ForeignKey(
        to='car_dealership.Car', on_delete=models.CASCADE, verbose_name='Car_model', related_name='car_model_for_dealer_price'
    )

    def __str__(self):
        return f"{self.car_price, self.car_model}"

    class Meta:
        db_table = 'dealer_price'
        verbose_name = 'Dealer price'
        verbose_name_plural = 'Dealers price'


class DealerSalesHistory(BaseModel):
    car = models.ForeignKey(to='car_dealership.Car', on_delete=models.CASCADE, verbose_name='Sold car', related_name='sold_car')
    dealership = models.ForeignKey(
        to='car_dealership.CarDealerShip', on_delete=models.CASCADE, verbose_name='Dealership which sold car',
        related_name='dealership_sold_car'
    )

    def __str__(self):
        return f"{self.car, self.dealership}"

    class Meta:
        db_table = 'dealer_sales_history'
        verbose_name = 'Dealer sales history'
        verbose_name_plural = 'Dealers sales history'
