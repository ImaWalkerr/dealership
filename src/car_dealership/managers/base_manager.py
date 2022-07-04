import logging
import random
import secrets
import string

from core.dumps import random_choices
from src.car_dealership.models import (
    Car,
    CarDealerShip,
    DealerShipGeneral,
)

from src.customer.models import Customer, CustomerCar
from src.dealer.models import Dealer, DealerGeneral


class BaseManager:
    """Work when starting project"""
    def __init__(self):
        self.letters = string.ascii_lowercase
        self.crypt = string.ascii_letters + string.digits
        self.length = 8
        self.value_min_id = 1
        self.value_max_id = 10
        self.value_min = 0
        self.value_max = 11
        self.car_value_max = 51

    def __generate_random_string(self):
        return ''.join(random.choice(self.letters) for _ in range(self.length))

    def __generate_crypt_string(self):
        return ''.join(secrets.choice(self.crypt) for _ in range(self.length))

    def handle(self):
        self.create_customer()
        self.create_car()
        self.create_dealer()
        self.create_dealer_general()
        self.create_dealership()
        self.create_dealership_general()
        self.create_customer_offer()

    def create_customer(self):
        for tick in range(1, self.value_max):
            logging.info(f'Creating customer #{tick}')
            Customer.objects.update_or_create(
                id=tick,
                defaults={
                    'username': start.__generate_random_string(),
                    'first_name': start.__generate_random_string(),
                    'last_name': start.__generate_random_string(),
                    'email': f'email_{tick}@gmail.com',
                    'is_staff': False,
                    'is_active': True,
                    'balance': random.randint(50000, 100000),
                    'car_features': {
                        'car_model': random_choices.random_car_model(),
                        'car_year': random.randint(1900, 2022),
                        'car_color': random_choices.random_car_color(),
                        'car_interior_color': random_choices.random_car_interior_color(),
                        'car_mileage': random.randint(self.value_min, 200000),
                        'car_body_type': random_choices.random_car_body_type(),
                        'car_engine_type': random_choices.random_car_engine_type(),
                        'car_engine_volume': random.randint(self.value_min, 8),
                        'car_gearbox': random_choices.random_car_gearbox(),
                        'number_of_doors': random.randint(self.value_min, 5),
                        'VIN': start.__generate_crypt_string(),
                        'electric_car': False
                    },
                }
            )

    def create_car(self):
        for tick in range(1, self.car_value_max):
            logging.info(f'Creating car #{tick}')
            Car.objects.update_or_create(
                id=tick,
                defaults={
                    'car_model': random_choices.random_car_model(),
                    'car_year': random.randint(1900, 2022),
                    'car_color': random_choices.random_car_color(),
                    'car_interior_color': random_choices.random_car_interior_color(),
                    'car_mileage': random.randint(self.value_min, 200000),
                    'car_body_type': random_choices.random_car_body_type(),
                    'car_engine_type': random_choices.random_car_engine_type(),
                    'car_engine_volume': random.randint(self.value_min, 8),
                    'car_gearbox': random_choices.random_car_engine_type(),
                    'number_of_doors': random.randint(self.value_min, 5),
                    'VIN': start.__generate_crypt_string(),
                    'electric_car': False,
                    'car_dealer_id': random.randint(self.value_min_id, self.value_max_id)
                }
            )

    def create_dealer(self):
        for tick in range(1, self.value_max):
            logging.info(f'Creating dealer #{tick}')
            Dealer.objects.update_or_create(
                id=tick,
                defaults={
                    'name': start.__generate_random_string(),
                    'founding_date': random.randint(1900, 2022),
                    'rating': random.randint(self.value_min, 100),
                    'cars_count': random.randint(self.value_min, 100),
                    'customers_count': random.randint(self.value_min, self.value_max)
                }
            )

    def create_dealer_general(self):
        for tick in range(1, self.value_max):
            logging.info(f'Creating dealer history #{tick}')
            DealerGeneral.objects.update_or_create(
                id=tick,
                defaults={
                    'dealer_id': random.randint(self.value_min_id, self.value_max_id),
                    'car_id': random.randint(self.value_min_id, self.value_max_id),
                    'car_price': random.randint(self.value_min, 50000),
                    'car_discount': random.randint(self.value_min, 15)
                }
            )

    def create_dealership(self):
        for tick in range(1, self.value_max):
            logging.info(f'Creating dealership #{tick}')
            CarDealerShip.objects.update_or_create(
                id=tick,
                defaults={
                    'name': start.__generate_random_string(),
                    'balance': random.randint(self.value_min, 100000)
                }
            )

    def create_dealership_general(self):
        for tick in range(1, self.value_max):
            logging.info(f'Creating dealership history #{tick}')
            DealerShipGeneral.objects.update_or_create(
                id=tick,
                defaults={
                    'car_id': random.randint(self.value_min_id, self.value_max_id),
                    'customer_id': random.randint(self.value_min_id, self.value_max_id),
                    'dealership_id': random.randint(self.value_min_id, self.value_max_id),
                }
            )

    def create_customer_offer(self):
        for tick in range(1, self.value_max):
            logging.info(f'Creating customer offers #{tick}')
            CustomerCar.objects.update_or_create(
                id=tick,
                defaults={
                    'customer_id': random.randint(self.value_min_id, self.value_max_id),
                    'car_id': random.randint(self.value_min_id, self.value_max_id),
                    'car_dealership_id': random.randint(self.value_min_id, self.value_max_id),
                    'discount': random.randint(self.value_min, 15),
                    'price': random.randint(1000, 100000),
                }
            )
        return 'Script successfully complete'


start = BaseManager()
