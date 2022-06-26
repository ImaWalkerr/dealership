from django.core.validators import RegexValidator
from django.db import models
from django_countries.fields import CountryField
from django_countries import Countries

from core.abstract_field import BaseModel


class G8Countries(Countries):
    """Countries choice"""
    only = ['CA', 'FR', 'DE', 'IT', 'JP', 'RU', 'GB']


class CarDealerShip(BaseModel):
    name = models.CharField(max_length=255, blank=True, verbose_name='Dealership name')
    country = CountryField(countries=G8Countries)  # default=None
    balance = models.FloatField(default=0, verbose_name='Dealership balance')
    cars_list = models.ManyToManyField(
        'Car', verbose_name='Car list for auto_show', related_name='dealership_car_list'
    )
    cars_sales_history = models.ManyToManyField(
        'CarDealerShipHistorySales', verbose_name='Car history sales', related_name='dealership_car_history_sales'
    )

    def __str__(self):
        return f"{self.name, self.balance}"

    class Meta:
        db_table = 'auto_show'
        verbose_name = 'AutoShow'
        verbose_name_plural = 'AutoShows'


class CarDealerShipHistorySales(BaseModel):
    customer = models.ForeignKey(to='customer.Customer', on_delete=models.CASCADE, verbose_name='Customer')
    car = models.ForeignKey('Car', on_delete=models.CASCADE, verbose_name='Car')

    def __str__(self):
        return f"{self.customer, self.car}"

    class Meta:
        db_table = 'auto_show_history'
        verbose_name = 'AutoShow History Sales'
        verbose_name_plural = 'AutoShows History Sales'


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


class CarInfo(BaseModel):

    GEARBOX = (
        ('AUTO', 'Automatic'),
        ('SEMI', 'Semi-automatic'),
        ('MEC', 'Mechanical'),
    )

    # for validating US VINs
    vehicle_number_validator = RegexValidator(regex=r'^[A-HJ-NPR-Z0-9]{17}$', message='Invalid Vehicle Number!')

    car_brand = models.CharField(max_length=255, blank=True, verbose_name='Car brand')
    car_year = models.PositiveIntegerField(default=None, blank=True, verbose_name='Car year')
    car_color = models.CharField(max_length=255, blank=True, verbose_name='Car color')
    car_interior_color = models.CharField(max_length=255, blank=True, verbose_name='Car interior color')
    car_mileage = models.IntegerField(default=0, blank=True, verbose_name='Car mileage')
    car_body_type = models.CharField(max_length=255, blank=True, verbose_name='Car body type')
    car_engine_type = models.CharField(max_length=255, blank=True, verbose_name='Car engine type')
    car_engine_volume = models.FloatField(default=None, blank=True, verbose_name='Car engine volume')
    car_gearbox = models.CharField(max_length=255, blank=True, choices=GEARBOX, verbose_name='Car drive')
    number_of_doors = models.PositiveIntegerField(default=True, blank=True, verbose_name='Number of doors')
    VIN = models.CharField(
        max_length=17, blank=True, validators=[vehicle_number_validator], verbose_name='Car VIN number'
    )

    def __str__(self):
        return f"{self.car_brand}"

    class Meta:
        db_table = 'cars_information'
        verbose_name = 'Car Information'
        verbose_name_plural = 'Cars Information'
