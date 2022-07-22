# class Car:
#     def __init__(self, max_speed: int):
#         self._max_speed = max_speed
#
#     def drive(self):
#         print('driving max speed' + str(self.max_speed))
#
#     @property
#     def max_speed(self):
#         return self._max_speed
#
#     @max_speed.setter
#     def max_speed(self, value):
#         self._max_speed = value

class Car:
    def __init__(self, max_speed: int):
        self.max_speed = max_speed

    def drive(self):
        print('driving max speed ' + str(self.max_speed))

    @property
    def max_speed(self):
        return self.__max_speed

    @max_speed.setter
    def max_speed(self, value):
        if value > 447:
            value = 447
        self.__max_speed = value


red = Car(500)
red.drive()


