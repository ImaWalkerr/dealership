from django.core.validators import RegexValidator, MinValueValidator
from django.db import models
from django_countries.fields import CountryField
from django_countries import Countries
from djmoney.models.fields import MoneyField

from core.abstract_field import BaseModel
from core.enum import (
    CarColor,
    CarInteriorColor,
    CarBodyType,
    CarEngineType,
    CarGearbox,
)


class G8Countries(Countries):
    """Countries choice"""
    only = ['CA', 'FR', 'DE', 'IT', 'JP', 'RU', 'GB']


class CarDealerShip(BaseModel):
    name = models.CharField(max_length=255, verbose_name='Dealership name')
    country = CountryField(countries=G8Countries)  # default=None
    balance = MoneyField(max_digits=14, decimal_places=2, default_currency='USD', verbose_name='Dealership balance')
    cars_list = models.ManyToManyField(
        'Car', through='DealerShipGeneral', verbose_name='Dealership car list', related_name='dealership_car_list'
    )

    def __str__(self):
        return f"{self.name, self.balance}"

    class Meta:
        db_table = 'dealership'
        verbose_name = 'Dealership'
        verbose_name_plural = 'Dealerships'
        ordering = ['id']


class DealerShipGeneral(BaseModel):
    dealership = models.ForeignKey(
        CarDealerShip, on_delete=models.SET_NULL, null=True, verbose_name='Dealership',
        related_name='dealership_general'
    )
    car = models.ForeignKey('Car', on_delete=models.SET_NULL, null=True, verbose_name='Car', related_name='car_general')
    customer = models.ForeignKey(
        to='customer.Customer', on_delete=models.SET_NULL, null=True, verbose_name='Customer', related_name='customer_general'
    )

    def __str__(self):
        return f"{self.car, self.dealership, self.customer}"

    class Meta:
        db_table = 'dealership_general'
        verbose_name = 'Dealership general'
        verbose_name_plural = 'Dealerships general'
        ordering = ['id']


class Car(BaseModel):
    car_model = models.CharField(max_length=255, verbose_name='Car model')
    car_info = models.ForeignKey(
        'CarInfo', on_delete=models.CASCADE, verbose_name='Car information', related_name='car_info'
    )
    car_dealer = models.ManyToManyField(to='dealer.Dealer', verbose_name='Car dealer', related_name='car_dealer')

    def __str__(self):
        return f"{self.car_model}"

    class Meta:
        db_table = 'cars'
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'
        ordering = ['id']


class CarInfo(BaseModel):

    # for validating US VINs
    vehicle_number_validator = RegexValidator(regex=r'^[A-HJ-NPR-Z0-9]{17}$', message='Invalid Vehicle Number!')

    car_brand = models.CharField(max_length=255, blank=True, verbose_name='Car brand')
    car_year = models.PositiveIntegerField(
        default=None, blank=True, validators=[MinValueValidator(1900)], verbose_name='Car year'
    )
    car_color = models.CharField(max_length=255, blank=True, choices=CarColor.choices(), verbose_name='Car color')
    car_interior_color = models.CharField(
        max_length=255, blank=True, choices=CarInteriorColor.choices(), verbose_name='Car interior color'
    )
    car_mileage = models.PositiveIntegerField(default=None, blank=True, verbose_name='Car mileage')
    car_body_type = models.CharField(
        max_length=255, blank=True, choices=CarBodyType.choices(), verbose_name='Car body type'
    )
    car_engine_type = models.CharField(
        max_length=255, blank=True, choices=CarEngineType.choices(), verbose_name='Car engine type'
    )
    car_engine_volume = models.FloatField(default=None, blank=True, verbose_name='Car engine volume')
    car_gearbox = models.CharField(max_length=255, blank=True, choices=CarGearbox.choices(), verbose_name='Car drive')
    number_of_doors = models.PositiveIntegerField(default=2, blank=True, verbose_name='Number of doors')
    VIN = models.CharField(
        max_length=17, blank=True, validators=[vehicle_number_validator], verbose_name='Car VIN number'
    )
    electric_car = models.BooleanField(default=False, verbose_name='Car type')

    def __str__(self):
        return f"{self.car_brand}"

    class Meta:
        db_table = 'cars_information'
        verbose_name = 'Car Information'
        verbose_name_plural = 'Cars Information'
        ordering = ['id']
