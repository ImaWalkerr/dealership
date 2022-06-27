import enum


class BaseClass(enum.Enum):

    @classmethod
    def choices(cls):
        return [(item.value, item.name) for item in cls]


class CarGearbox(BaseClass):
    AUTOMATIC = 'automatic'
    SEMI_AUTOMATIC = 'semi-automatic'
    MECHANICAL = 'mechanical'


class CarColor(BaseClass):
    YELLOW = 'yellow'
    ORANGE = 'orange'
    RED = 'red'
    WHITE = 'white'
    BLACK = 'black'
    BLUE = 'blue'
    GREY = 'grey'
    GREEN = 'green'


class CarInteriorColor(BaseClass):
    BLACK = 'black'
    BROWN = 'brown'
    BEIGE = 'beige'
    WHITE = 'white'


class CarBodyType(BaseClass):
    SEDAN = 'sedan'
    UNIVERSAL = 'universal'
    HATCHBACK = 'hatchback'
    MINIVAN = 'minivan'
    SUV = 'SUV(crossover)'
    COUPE = 'coupe'
    CABRIOLET = 'cabriolet'
    PICKUP = 'pickup'


class CarEngineType(BaseClass):
    STRAIGHT = 'straight'
    INLINE = 'inline'
    V = 'V'
    FLAT = 'flat'
