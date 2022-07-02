from src.dealer.models import DealerGeneral
from src.customer.models import Customer, CustomerCar
from src.car_dealership.models import Car, DealerShipGeneral
from django.db.models import Q


class BuyingCars:
    def buying_cars(self):
        for customer in Customer.objects.all():
            customer_car = customer.car_features

            search_car_for_customer = (
                    Q(car_model__contains=customer_car.get('car_model'))
                    & Q(car_year__gte=customer_car.get('car_year'))
                    & Q(car_color__contains=customer_car.get('car_color'))
                    & Q(car_interior_color__contains=customer_car.get('car_interior_color'))
                    & Q(car_mileage__lte=customer_car.get('car_mileage'))
                    & Q(car_body_type__contains=customer_car.get('car_body_type'))
                    & Q(car_engine_type__contains=customer_car.get('car_engine_type'))
                    & Q(car_engine_volume__exact=customer_car.get('car_engine_volume'))
                    & Q(car_gearbox__contains=customer_car.get('car_gearbox'))
                    & Q(number_of_doors__exact=customer_car.get('number_of_doors'))
                    & Q(VIN__exact=customer_car.get('VIN'))
                    & Q(electric_car__exact=customer_car.get('electric_car'))
            )
            sorted_cars = Car.objects.filter(search_car_for_customer).order_by('car_model')

            if sorted_cars:
                for car in sorted_cars:
                    if customer.balance > 0:
                        for dealership in DealerShipGeneral.objects.filter(car_id=car.id):
                            for dealer in DealerGeneral.objects.filter(car_id=car.id):
                                dealer_price = dealer.car_price
                                dealer_discount = dealer.car_discount
                                car_price = dealer_price * ((100 - dealer_discount) / 100)
                                if customer.balance >= car_price:
                                    sold_car = CustomerCar.objects.create(
                                        customer=customer.id,
                                        car=car.id,
                                        car_dealership=dealership.id,
                                        price=car_price,
                                        discount=dealer_discount
                                    )
                                    customer_new_balance = customer.balance - car_price
                                    customer = Customer.objects.update(
                                        balance=customer_new_balance
                                    )
                                    dealer_history = DealerGeneral.objects.create(
                                        car=car.id,
                                        dealer=dealer.id,
                                        car_price=car_price,
                                        car_discount=dealer_discount
                                    )
                                    dealership_history = DealerShipGeneral.objects.create(
                                        dealership=dealership.id,
                                        car=car.id,
                                        customer=customer.id
                                    )
                                else:
                                    continue
                    else:
                        continue
            else:
                continue


buying_cars_process = BuyingCars()
