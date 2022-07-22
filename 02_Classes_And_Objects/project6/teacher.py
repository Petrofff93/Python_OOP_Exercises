from project6.employee import Employee
from project6.person import Person


class Teacher(Person, Employee):
    def teach(self):
        return 'teaching...'

