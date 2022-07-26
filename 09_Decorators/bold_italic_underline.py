def make_underline(func):
    def wrapper(*args):
        func_result = func(*args)
        return f"<u>{func_result}</u>"

    return wrapper


def make_italic(func):
    def wrapper(*args):
        func_result = func(*args)
        return f"<i>{func_result}</i>"

    return wrapper


def make_bold(func):
    def wrapper(*args):
        func_result = func(*args)
        return f"<b>{func_result}</b>"
    return wrapper


@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello , {name}"


print(greet("Peter"))
