from project.animals.animal import Bird


class Owl(Bird):
    @property
    def allowed_foods(self):
        return ["Meat"]

    @property
    def weight_incremental(self):
        return 0.25

    @staticmethod
    def make_sound():
        return "Hoot Hoot"


class Hen(Bird):
    @property
    def allowed_foods(self):
        return ["Meat", "Fruit", "Vegetable", "Seed"]

    @property
    def weight_incremental(self):
        return 0.35

    @staticmethod
    def make_sound():
        return "Cluck"
