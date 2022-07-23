from abc import ABC, abstractmethod

from project.food import Food


class Animal(ABC):
    def __init__(self, name, weight, food_eaten):
        self.name = name
        self.weight = weight
        self.food_eaten = food_eaten

    @property
    @abstractmethod
    def allowed_foods(self):
        pass

    @abstractmethod
    def make_sound(self):
        pass

    def feed(self, food: Food):
        pass


class Bird(Animal):
    @abstractmethod
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.wing_size = float()


class Mammal(Animal):
    @abstractmethod
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.living_region = str()
