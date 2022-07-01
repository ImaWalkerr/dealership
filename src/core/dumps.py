import random


class ChoicesForRandom:
    def __init__(self):
        self.car_models = (
            'BWM', 'FORD', 'MERCEDES_BENZ', 'NISSAN', 'HONDA', 'PORSCHE', 'SAAB', 'DODGE', 'PONTIAC', 'CHEVROLET',
        )
        self.car_gearbox = (
            'AUTOMATIC', 'SEMI_AUTOMATIC', 'MECHANICAL',
        )
        self.car_color = (
            'YELLOW', 'ORANGE', 'RED', 'WHITE', 'BLACK', 'BLUE', 'GREY', 'GREEN',
        )
        self.car_interior_color = (
            'BLACK', 'BROWN', 'BEIGE', 'WHITE',
        )
        self.car_body_type = (
            'SEDAN', 'UNIVERSAL', 'HATCHBACK', 'MINIVAN', 'SUV', 'COUPE', 'CABRIOLET', 'PICKUP',
        )
        self.car_engine_type = (
            'STRAIGHT', 'INLINE', 'V', 'FLAT',
        )

    def random_car_model(self):
        return random.choice(self.car_models)

    def random_car_gearbox(self):
        return random.choice(self.car_gearbox)

    def random_car_color(self):
        return random.choice(self.car_color)

    def random_car_interior_color(self):
        return random.choice(self.car_interior_color)

    def random_car_body_type(self):
        return random.choice(self.car_body_type)

    def random_car_engine_type(self):
        return random.choice(self.car_engine_type)


random_choices = ChoicesForRandom()
