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
        total_salaries = sum(s.salary for s in self.workers)

        if self.__budget >= total_salaries:
            self.__budget -= total_salaries
            return f'You payed your workers. They are happy. Budget left: {self.__budget}'
        return 'You have no budget to pay your workers. They are unhappy'

    def tend_animals(self):
        total_animal_tend = sum(x.money_for_care for x in self.animals)

        if self.__budget >= total_animal_tend:
            self.__budget -= total_animal_tend
            return f'You tended all the animals. They are happy. Budget left: {self.__budget}'
        return 'You have no budget to tend the animals. They are unhappy.'

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f'You have {len(self.animals)} animals\n'
        lions = [repr(x) for x in self.animals if isinstance(x, Lion)]
        result += f'----- {len(lions)} Lions:\n' + '\n'.join(lions) + '\n'

        tigers = [repr(x) for x in self.animals if isinstance(x, Tiger)]
        result += f'----- {len(tigers)} Tigers:\n' + '\n'.join(tigers) + '\n'

        cheetahs = [repr(x) for x in self.animals if isinstance(x, Cheetah)]
        result += f'----- {len(cheetahs)} Cheetahs:\n' + '\n'.join(cheetahs)

        return result

    def workers_status(self):
        result = f'You have {len(self.workers)} workers\n'
        keepers = [repr(x) for x in self.workers if isinstance(x, Keeper)]
        result += f'----- {len(keepers)} Keepers:\n' + '\n'.join(keepers) + '\n'

        caretakers = [repr(x) for x in self.workers if isinstance(x, Caretaker)]
        result += f'----- {len(caretakers)} Caretakers:\n' + '\n'.join(caretakers) + '\n'

        vets = [repr(x) for x in self.workers if isinstance(x, Vet)]
        result += f'----- {len(vets)} Vets:\n' + '\n'.join(vets)

        return result

