def logged(func):
    def wrapper(*args, **kwargs):
        func_name = func.__name__
        func_result = func(*args, **kwargs)
        return f"you called {func_name}{args}\nit returned {func_result}"

    return wrapper


@logged
def sum_func(a, b):
    return a + b


print(sum_func(1, 4))
