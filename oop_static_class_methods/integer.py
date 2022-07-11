import math


class Integer:
    def __init__(self, value):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if not isinstance(float_value, float):
            return 'value is not a float'
        return cls(math.floor(float_value))

    @classmethod
    def from_roman(cls, value):

        l = list()

        form = 0

        for i in range(0, len(value)):
            if value[i] == 'I':
                l.append(int(1))
            elif value[i] == 'V':
                l.append(int(5))
            elif value[i] == 'X':
                l.append(int(10))
            elif value[i] == 'L':
                l.append(int(50))
            elif value[i] == 'C':
                l.append(int(100))
            elif value[i] == 'D':
                l.append(int(500))
            elif value[i] == 'M':
                l.append(int(1000))

        i = 0
        while i < len(l) - 1:
            if l[i] < l[i + 1]:
                form = form + l[i + 1] - l[i]
                i = i + 2
            else:
                form = form + l[i]
                i = i + 1

        if i == len(l):
            if l[i - 2] == l[i - 1]:
                form = form + l[i - 1]
        else:
            form = form + l[i]

        return cls(form)

    @classmethod
    def from_string(cls, value):
        if isinstance(value, str):
            try:
                return cls(int(value))
            except Exception:
                return 'wrong type'
        return 'wrong type'


first_num = Integer(10)
print(first_num.value)

second_num = Integer.from_roman("IV")
print(second_num.value)

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))
