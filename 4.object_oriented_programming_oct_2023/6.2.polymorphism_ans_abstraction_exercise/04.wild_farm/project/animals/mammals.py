from project.animals.animal import Mammal


class Mouse(Mammal):
    ALLOWED_FOOD = ["Vegetable", "Fruit"]
    WEIGHT_INCREMENT = 0.10

    def make_sound(self):
        return "Squeak"


class Dog(Mammal):
    ALLOWED_FOOD = ["Meat"]
    WEIGHT_INCREMENT = 0.40

    def make_sound(self):
        return "Woof!"


class Cat(Mammal):
    ALLOWED_FOOD = ["Vegetable", "Meat"]
    WEIGHT_INCREMENT = 0.30

    def make_sound(self):
        return "Meow"


class Tiger(Mammal):
    ALLOWED_FOOD = ["Meat"]
    WEIGHT_INCREMENT = 1.00

    def make_sound(self):
        return "ROAR!!!"
