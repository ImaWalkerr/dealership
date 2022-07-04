from django.contrib import admin
from django.db.models import Avg

from src.car_dealership.models import (
    CarDealerShip,
    DealerShipGeneral,
    Car,
)


@admin.register(CarDealerShip)
class CarDealerShipAdmin(admin.ModelAdmin):
    fieldsets = (
        ('DealerShip', {
            'fields': ('name', 'country', 'balance',)
        }),
        ('Other', {
            'fields': ('car_list',)
        }),
    )
    list_display = ('name', 'country', 'balance',)
    list_filter = ('name', 'country',)
    search_fields = ('name',)
    list_display_links = ('name',)


@admin.register(DealerShipGeneral)
class DealerShipGeneralAdmin(admin.ModelAdmin):
    fieldsets = (
        ('DealerShip history sale', {
            'fields': ('dealership', 'car', 'customer',)
        }),
    )
    list_display = ('dealership',)
    list_filter = ('dealership',)
    search_fields = ('dealership',)
    list_display_links = ('dealership',)


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Car', {
            'fields': ('car_model', 'car_dealer',)
        }),
        ('Car info block 1', {
            'fields': ('car_year', 'car_color', 'car_interior_color',)
        }),
        ('Car info block 2', {
            'fields': ('car_mileage', 'car_body_type', 'car_engine_type', 'car_engine_volume',)
        }),
        ('Car info block 3', {
            'fields': ('car_gearbox', 'number_of_doors', 'VIN', 'electric_car',)
        }),
    )
    list_display = ('car_model', 'car_dealer', 'car_year', 'avg_car_mileage', 'avg_car_year', 'amount_of_cars',)
    list_display_links = ('car_model',)
    list_filter = ('car_model', 'car_dealer',)
    search_fields = ('car_model',)

    def avg_car_mileage(self, obj):
        car_mileage = Car.objects.all().values('car_mileage').aggregate(Avg('car_mileage'))
        try:
            return car_mileage.get('car_mileage__avg')
        except AttributeError:
            return None

    avg_car_mileage.short_description = 'avg car mileage'

    def avg_car_year(self, obj):
        car_year = Car.objects.all().values('car_year').aggregate(Avg('car_year'))
        try:
            return car_year.get('car_year__avg')
        except AttributeError:
            return None

    avg_car_year.short_description = 'avg car year'

    def amount_of_cars(self, obj):
        try:
            return Car.objects.filter(car_model=obj.car_model).count()
        except AttributeError:
            return None

    amount_of_cars.short_description = 'amount of cars'
