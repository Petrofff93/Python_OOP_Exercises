def genrange(start, end):
    start_num = start
    end_num = end

    while start_num < end_num + 1:
        yield start_num
        start_num += 1


print(list(genrange(1, 10)))