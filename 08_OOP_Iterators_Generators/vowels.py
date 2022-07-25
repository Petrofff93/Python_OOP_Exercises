class vowels:
    vowel_chars = 'eyuioa'

    def __init__(self, string_sequence):
        self.string_sequence = string_sequence
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.idx < len(self.string_sequence):
            if self.string_sequence[self.idx].lower() not in self.vowel_chars:
                self.idx += 1
                continue
            value_to_return = self.string_sequence[self.idx]
            self.idx += 1
            return value_to_return
        raise StopIteration


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
