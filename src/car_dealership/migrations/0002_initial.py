# Generated by Django 4.0.4 on 2022-07-01 13:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('car_dealership', '0001_initial'),
        ('dealer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dealershipgeneral',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='customer_general', to=settings.AUTH_USER_MODEL, verbose_name='Customer'),
        ),
        migrations.AddField(
            model_name='dealershipgeneral',
            name='dealership',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dealership_general', to='car_dealership.cardealership', verbose_name='Dealership'),
        ),
        migrations.AddField(
            model_name='cardealership',
            name='cars_list',
            field=models.ManyToManyField(related_name='dealership_car_list', through='car_dealership.DealerShipGeneral', to='car_dealership.car', verbose_name='Dealership car list'),
        ),
        migrations.AddField(
            model_name='car',
            name='car_dealer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='car_dealer', to='dealer.dealer', verbose_name='Car dealer'),
        ),
    ]
