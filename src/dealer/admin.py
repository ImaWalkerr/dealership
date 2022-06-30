from django.contrib import admin

from src.dealer.models import Dealer, DealerGeneral


@admin.register(Dealer)
class DealerAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Main', {
            'fields': ('name', 'founding_date', 'rating',)
        }),
        ('Other', {
            'fields': ('cars_count',)
        }),
    )

    list_display = ('name', 'founding_date', 'rating',)
    list_filter = ('name', 'rating',)
    search_fields = ('name',)
    list_display_links = ('name',)


@admin.register(DealerGeneral)
class DealerGeneralAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Main', {
            'fields': ('car', 'dealer',)
        }),
        ('Price', {
            'fields': ('car_price', 'car_discount',)
        }),
    )

    list_display = ('car', 'dealer', 'car_price',)
    list_filter = ('car', 'dealer',)
    search_fields = ('car', 'dealer',)
    list_display_links = ('car',)
