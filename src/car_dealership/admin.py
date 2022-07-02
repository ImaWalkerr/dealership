from django.contrib import admin

from src.car_dealership.models import (
    CarDealerShip,
    DealerShipGeneral,
    Car,
)


@admin.register(CarDealerShip)
class CarDealerShipAdmin(admin.ModelAdmin):
    fieldsets = (
        ('DealerShip', {
            'fields': ('name', 'country', 'balance')
        }),
        ('Other', {
            'fields': ('car_list',)
        }),
    )
    list_display = ('name', 'country', 'balance')
    list_filter = ('name', 'country')
    search_fields = ('name',)
    list_display_links = ('name',)


@admin.register(DealerShipGeneral)
class DealerShipGeneralAdmin(admin.ModelAdmin):
    fieldsets = (
        ('DealerShip history sale', {
            'fields': ('dealership', 'car', 'customer')
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
            'fields': ('car_model', 'car_dealer')
        }),
        ('Car info block 1', {
            'fields': ('car_year', 'car_color', 'car_interior_color')
        }),
        ('Car info block 2', {
            'fields': ('car_mileage', 'car_body_type', 'car_engine_type', 'car_engine_volume')
        }),
        ('Car info block 3', {
            'fields': ('car_gearbox', 'number_of_doors', 'VIN', 'electric_car')
        }),
    )
    list_filter = ('car_model', 'car_dealer')
    search_fields = ('car_model',)
