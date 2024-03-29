from project.animals.animal import Mammal


class Mouse(Mammal):
    @property
    def allowed_foods(self):
        return ["Vegetable", "Fruit"]

    @property
    def weight_incremental(self):
        return 0.1

    def make_sound(self):
        return "Squeak"


class Dog(Mammal):
    @property
    def allowed_foods(self):
        return ["Meat"]

    @property
    def weight_incremental(self):
        return 0.4

    @staticmethod
    def make_sound():
        return "Woof!"


class Cat(Mammal):
    @property
    def allowed_foods(self):
        return ["Vegetable", "Meat"]

    @property
    def weight_incremental(self):
        return 0.3

    @staticmethod
    def make_sound():
        return "Meow"


class Tiger(Mammal):
    @property
    def allowed_foods(self):
        return ["Meat"]

    @property
    def weight_incremental(self):
        return 1

    @staticmethod
    def make_sound():
        return "ROAR!!!"
