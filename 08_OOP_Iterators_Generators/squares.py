def squares(n):
    value = 1

    while value < n + 1:
        yield value ** 2
        value += 1


print(list(squares(5)))