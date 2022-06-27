from django.contrib import admin

from customer.models import *


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Customer', {
            'fields': ('first_name', 'last_name', 'email', 'birthday')
        }),
        ('Main', {
            'fields': ('balance', 'purchase_history')
        })
    )

    list_display = ('first_name', 'last_name')
    list_filter = ('first_name', 'balance')
    search_fields = ('first_name',)
    list_display_links = ('first_name',)


@admin.register(CustomerCar)
class CustomerCarAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Customer', {
            'fields': ('customer',)
        }),
        ('Car', {
            'fields': ('car', 'car_features', 'car_dealership')
        }),
        ('Price', {
            'fields': ('discount', 'price')
        })
    )

    list_display = ('customer', 'car')
    list_filter = ('customer', 'car', 'price')
    search_fields = ('customer', 'car')
    list_display_links = ('customer',)
