from django.contrib import admin
from django.db.models import Avg, Count

from src.customer.models import Customer, CustomerCar


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Customer', {
            'fields': ('first_name', 'last_name', 'email', 'birthday',)
        }),
        ('Main', {
            'fields': ('balance', 'purchase_history',)
        })
    )
    list_display = (
        'first_name', 'last_name', 'customer_avg_balance', 'popular_car', 'customer_car_count', 'avg_car_price',
        'avg_car_discount',
    )
    list_filter = ('first_name', 'balance',)
    search_fields = ('first_name',)
    list_display_links = ('first_name',)

    def popular_car(self, obj):
        car_models = CustomerCar.objects.all().annotate(Count('car__car_model')).order_by()
        try:
            return car_models.values_list('car__car_model', flat=True)[0]
        except AttributeError:
            return None

    popular_car.short_description = 'popular car'

    def customer_avg_balance(self, obj):
        customer_balance = Customer.objects.all().values('balance').aggregate(Avg('balance'))
        try:
            return round(customer_balance.get('balance__avg'))
        except AttributeError:
            return None

    customer_avg_balance.short_description = 'avg customer balance'

    def customer_car_count(self, obj):
        try:
            return CustomerCar.objects.filter(customer_id=obj.id).count()
        except AttributeError:
            return None

    customer_car_count.short_description = 'amount of cars'

    def avg_car_price(self, obj):
        car_price = CustomerCar.objects.all().values('price').aggregate(Avg('price'))
        try:
            return round(car_price.get('price__avg'))
        except AttributeError:
            return None

    avg_car_price.short_decription = 'avg car price'

    def avg_car_discount(self, obj):
        car_discount = CustomerCar.objects.all().values('discount').aggregate(Avg('discount'))
        try:
            return car_discount.get('discount__avg')
        except AttributeError:
            return None

    avg_car_discount.short_description = 'avg car discount %'


@admin.register(CustomerCar)
class CustomerCarAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Customer', {
            'fields': ('customer',)
        }),
        ('Car', {
            'fields': ('car', 'car_dealership',)
        }),
        ('Price', {
            'fields': ('discount', 'price',)
        })
    )
    list_display = ('customer', 'car',)
    list_filter = ('customer', 'car', 'price',)
    search_fields = ('customer', 'car',)
    list_display_links = ('customer',)
