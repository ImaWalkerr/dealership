import random
import secrets
import string

from car_dealership.models import (
    Car,
    CarInfo,
    CarDealerShip,
    G8Countries,
)
from core.enum import (
    CarModels,
    CarColor,
    CarInteriorColor,
    CarBodyType,
    CarEngineType,
    CarGearbox,
)
from customer.models import Customer
from dealer.models import Dealer, DealerGeneral


class BaseManager:
    """Work when starting project"""
    def __init__(self):
        self.letters = string.ascii_lowercase
        self.crypt = string.ascii_letters + string.digits
        self.length = 8
        self.value_min = 0
        self.value_max = 10

    def __generate_random_string(self):
        return ''.join(random.choice(self.letters) for _ in range(self.length))

    def __generate_crypt_string(self):
        return ''.join(secrets.choice(self.crypt) for _ in range(self.length))

    def __random_car_model(self):
        return random.choice(list(CarModels))

    def __random_car_color(self):
        return random.choice(list(CarColor))

    def __random_interior_color(self):
        return random.choice(list(CarInteriorColor))

    def __random_car_body_type(self):
        return random.choice(list(CarBodyType))

    def __random_car_engine_type(self):
        return random.choice(list(CarEngineType))

    def __random_car_gearbox(self):
        return random.choice(list(CarGearbox))

    def handle(self):
        self.create_car()
        self.create_car_info()
        self.create_customer()
        self.create_dealer()
        self.create_dealer_general()
        self.create_dealership()
        self.create_dealership_general()
        self.create_customer_offer()

    def create_car(self):
        for tick in range(self.value_max):
            car = Car.objects.update_or_create(
                is_active=True,
                car_model=start.__random_car_model()
            )
            car.save()

    def create_car_info(self):
        car_list = Car.objects.all()
        for car in car_list:
            for el in range(self.value_max):
                CarInfo.objects.update_or_create(
                    is_active=True,
                    car_brand=start.__generate_random_string(),
                    car_year=random.randint(1900, 2022),
                    car_color=start.__random_car_color(),
                    car_interior_color=start.__random_interior_color(),
                    car_mileage=random.randint(self.value_min, 200000),
                    car_body_type=start.__random_car_body_type(),
                    car_engine_type=start.__random_car_engine_type(),
                    car_engine_volume=random.randint(self.value_min, 8),
                    car_gearbox=start.__random_car_gearbox(),
                    number_of_doors=random.randint(self.value_min, 5),
                    VIN=start.__generate_crypt_string(),
                    electric_car=False,
                    car=car
                )

    def create_customer(self):
        for tick in range(self.value_max):
            customer = Customer.objects.update_or_create(
                username=start.__generate_random_string(),
                first_name=start.__generate_random_string(),
                last_name=start.__generate_random_string(),
                email=f'email_{tick}@gmail.com',
                is_staff=False,
                is_active=True,
                balance=random.randint(self.value_min, 10000)
            )
            customer.set_password('customer')
            customer.save()

    def create_dealer(self):
        for tick in range(self.value_max):
            dealer = Dealer.objects.update_or_create(
                is_active=True,
                name=start.__generate_random_string(),
                founding_date=random.randint(1900, 2022),
                rating=random.randint(self.value_min, 100),
                cars_count=random.randint(self.value_min, 100)
            )
            dealer.save()

    def create_dealer_general(self):
        dealer_list = Dealer.objects.all()
        for dealer in dealer_list:
            for el in range(self.value_max):
                DealerGeneral.objects.update_or_create(
                    dealer_id=random.randint(self.value_min, self.value_max),
                    car_id=random.randint(self.value_min, self.value_max),
                    car_price=random.randint(self.value_min, 1000000),
                    car_discount=random.randint(self.value_min, 15),
                    dealer=dealer
                )

    def create_dealership(self):
        for tick in range(self.value_max):
            dealership = CarDealerShip.objects.update_or_create(
                is_active=True,
                name=start.__generate_random_string(),
                country=random.choice(G8Countries),
                balance=random.randint(self.value_min, 100000)
            )
            dealership.save()

    def create_dealership_general(self):
        dealership_list = CarDealerShip.objects.all()
        for dealership in dealership_list:
            for el in range(self.value_max):
                DealerGeneral.objects.update_or_create(
                    is_active=True,
                    car_id=random.randint(self.value_min, self.value_max),
                    customer_id=random.randint(self.value_min, self.value_max),
                    dealership_id=random.randint(self.value_min, self.value_max),
                    dealership=dealership
                )

    def create_customer_offer(self):
        customer_list = Customer.objects.all()
        for customer in customer_list:
            for el in range(self.value_max):
                Customer.objects.update_or_create(
                    is_active=True,
                    car_features={
                        'model': start.__random_car_model(),
                        'color': start.__random_car_color(),
                        'interior': start.__random_interior_color(),
                        'body_type': start.__random_car_body_type(),
                        'engine_type': start.__random_car_engine_type()
                    },
                    discount=random.randint(self.value_min, 15),
                    price=random.randint(1000, 1000000),
                    car_id=random.randint(self.value_min, self.value_max),
                    car_dealership_id=random.randint(self.value_min, self.value_max),
                    customer_id=random.randint(self.value_min, self.value_max),
                    customer=customer
                )

        return 'Script successfully complete'


start = BaseManager()
