def tags(tag_name):
    def decorator(func_ref):
        def wrapper(*args):
            func_res = func_ref(*args)
            return f"<{tag_name}>{func_res}</{tag_name}>"
        return wrapper
    return decorator


@tags('h1')
def to_upper(text):
    return text.upper()


print(to_upper('hello'))

