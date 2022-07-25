class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self):
        value_to_return = self.start

        while self.start // self.step < self.count:
            self.start += self.step
            return value_to_return
        raise StopIteration


numbers = take_skip(2, 6)
for number in numbers:
    print(number)


