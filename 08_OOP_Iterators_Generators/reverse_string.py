def reverse_text(text):
    start = -1

    while start >= -len(text):
        yield text[start]
        start -= 1


for char in reverse_text("step"):
    print(char, end='')
