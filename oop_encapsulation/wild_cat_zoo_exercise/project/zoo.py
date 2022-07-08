from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__budget < price:
            return 'Not enough budget'
        elif self.__animal_capacity < len(self.animals) + 1:
            return 'Not enough space for animal'

        self.__budget -= price
        self.animals.append(animal)
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker):
        if self.__workers_capacity >= len(self.workers) + 1:
            self.workers.append(worker)
            return f'{worker.name} the {worker.__class__.__name__} hired successfully'
        return 'Not enough space for worker'

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f'{worker_name} fired successfully'
        return f'There is no {worker_name} in the zoo'

    def pay_workers(self):
        total_salaries = 0
        for worker in self.workers:
            total_salaries += worker.salary

        if self.__budget >= total_salaries:
            self.__budget -= total_salaries
            return f'You payed your workers. They are happy. Budget left: {self.__budget}'
        return 'You have no budget to pay your workers. They are unhappy'

    def tend_animals(self):
        total_animal_tend = 0
        for animal in self.animals:
            total_animal_tend += animal.money_for_care

        if self.__budget >= total_animal_tend:
            self.__budget -= total_animal_tend
            return f'You tended all the animals. They are happy. Budget left: {self.__budget}'
        return 'You have no budget to tend the animals. They are unhappy.'

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f'You have {len(self.animals)} animals\n'

        lions = [x for x in self.animals if type(x) == Lion]
        tigers = [x for x in self.animals if type(x) == Tiger]
        cheetahs = [x for x in self.animals if type(x) == Cheetah]

        result += f'----- {len(lions)} Lions:\n'

        for lion in lions:
            result += f'{repr(lion)}\n'

        result += f'----- {len(tigers)} Tigers:\n'

        for tiger in tigers:
            result += f'{repr(tiger)}\n'

        result += f'----- {len(cheetahs)} Cheetahs:\n'

        for cheetah in cheetahs:
            result += f'{repr(cheetah)}\n'

        return result.strip()

    def workers_status(self):
        result = f'You have {len(self.workers)} workers\n'

        keepers = [x for x in self.workers if type(x) == Keeper]
        caretakers = [x for x in self.workers if type(x) == Caretaker]
        vets = [x for x in self.workers if type(x) == Vet]

        result += f'----- {len(keepers)} Keepers:\n'

        for keeper in keepers:
            result += f'{repr(keeper)}\n'

        result += f'----- {len(caretakers)} Caretakers:\n'

        for caretaker in caretakers:
            result += f'{repr(caretaker)}\n'

        result += f'----- {len(vets)} Vets:\n'

        for vet in vets:
            result += f'{repr(vet)}\n'

        return result.strip()
