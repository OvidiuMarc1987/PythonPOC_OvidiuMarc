from functools import wraps
registry_list = []


def registry(fnc):
    registry_list.append(fnc.__name__)
    print(registry_list)

    @wraps(fnc)
    def wrapped(*args, **kwargs):
        return fnc(*args, **kwargs)
    return wrapped


@registry
def uppercase(fn):
    @wraps(fn)
    def wrapped(*args, **kwargs):
        return fn(*args, **kwargs).upper()
    return wrapped


@registry
def safe_addition(fnc):
    def wrapper_arguments(arg1, arg2):
        result = round(fnc(arg1, arg2), 2)
        return result
    return wrapper_arguments


@safe_addition
def calculator(first_number, second_number):
    return first_number + second_number


@uppercase 
def get_string(string):
    return string


res = get_string("test")
print(res)

res2 = calculator(4.9, -4.8)
print(res2)
