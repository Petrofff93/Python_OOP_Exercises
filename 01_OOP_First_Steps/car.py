class Car:
    def __init__(self, name, model, engine):
        self.name = name
        self.model = model
        self.engine = engine

    def get_info(self):
        return f"This is {self.name} {self.model} with engine {self.engine}"


my_car = Car('Opel', 'Corsa', '1.2L Petrol')
print(my_car.get_info())
