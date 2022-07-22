from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    def __init__(self, fq, fc):
        self.fuel_quantity = fq
        self.fuel_consumption = fc

    def drive(self, distance):
        total_consumption = (self.fuel_consumption + 0.9) * distance

        if total_consumption <= self.fuel_quantity:
            self.fuel_quantity -= total_consumption

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    def __init__(self, fq, fc):
        self.fuel_quantity = fq
        self.fuel_consumption = fc

    def drive(self, distance):
        total_consumption = (self.fuel_consumption + 1.6) * distance

        if total_consumption <= self.fuel_quantity:
            self.fuel_quantity -= total_consumption

    def refuel(self, fuel):
        self.fuel_quantity += (fuel * 0.95)


truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)

