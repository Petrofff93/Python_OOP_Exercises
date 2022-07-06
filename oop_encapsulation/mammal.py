class Mammal:
    __kingdom = 'animals'

    def __init__(self, name, type, sound):
        self.name = name
        self.type = type
        self.sound = sound

    def make_sound(self):
        return self.sound

    def get_kingdom(self):
        return self.__kingdom

    def info(self):
        return f'{self.name} is of type {self.type}'


m = Mammal('gosho', 'bear', 'grrr')
print(m.get_kingdom())