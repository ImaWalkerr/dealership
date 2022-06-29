from django.contrib import admin

from src.car_dealership.models import (
    CarDealerShip,
    DealerShipGeneral,
    Car,
    CarInfo
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
            'fields': ('car_model', 'car_info', 'car_dealer')
        }),
    )
    list_filter = ('car_model', 'car_dealer')
    search_fields = ('car_model',)


@admin.register(CarInfo)
class CarInfoAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Car info block 1', {
            'fields': ('car_brand', 'car_year', 'car_color', 'car_interior_color')
        }),
        ('Car info block 2', {
            'fields': ('car_mileage', 'car_body_type', 'car_engine_type', 'car_engine_volume')
        }),
        ('Car info block 3', {
            'fields': ('car_gearbox', 'number_of_doors', 'VIN', 'electric_car')
        }),
    )
    list_display = ('car_brand', 'car_year', 'car_body_type', 'car_engine_type', 'car_gearbox')
    list_filter = ('car_brand', 'car_year', 'car_body_type', 'car_engine_type', 'car_gearbox', 'electric_car')
    search_fields = ('car_brand', 'car_year', 'VIN')
    list_display_links = ('car_brand',)
