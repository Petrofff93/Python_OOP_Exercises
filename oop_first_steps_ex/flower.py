class Flower:
    def __init__(self, name, water_requirements):
        self.name = name
        self.water_requirements = water_requirements
        self.is_happy = False

    def water(self, quantity):
        if quantity >= self.water_requirements:
            self.is_happy = True

    def status(self):
        if self.is_happy:
            return f'{self.name} is happy'
        else:
            return f'{self.name} is not happy'


f = Flower('Lilly', 100)
f.water(50)
print(f.status())
f.water(60)
print(f.status())
f.water(100)
print(f.status())
