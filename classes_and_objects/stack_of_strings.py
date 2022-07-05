class Stack:
    def __init__(self):
        self.data = []

    @staticmethod
    def check_if_string(element):
        return isinstance(element, str)

    def push(self, element):
        if self.check_if_string(element):
            self.data.append(element)

    def pop(self):
        last_element = self.data.pop()
        return last_element

    def top(self):
        element = self.data[-1]
        return element

    def is_empty(self):
        return len(self.data) == 0

    def __str__(self):
        stack_data = f"[{', '.join(reversed(self.data))}]"
        return stack_data
