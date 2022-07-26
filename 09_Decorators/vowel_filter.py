def vowel_filter(func):
    def wrapper():
        result = [x for x in func() if x.lower() in 'aeoui']
        return result

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
