from project.animal import Animal


class Cheetah(Animal):
    __money_for_care = 60

    def __init__(self, name, gender, age, money_for_care=__money_for_care):
        super().__init__(name, gender, age, money_for_care)

