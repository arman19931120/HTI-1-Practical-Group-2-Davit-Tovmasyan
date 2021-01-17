import time

from functools import wraps


def time_it(func):
    @wraps(func)
    def inner(*args, **kwargs):
        start = time.time()

        result = func(*args, **kwargs)

        time_needed = time.time() - start
        print(f'{func.__name__} with {args} {kwargs} arguments took {time_needed} seconds.')

        return result

    # inner = wraps(func)(inner)
    # inner.__name__ = func.__name__
    # inner.__doc__ = func.__doc__
    return inner


@time_it
def div(x, y):
    return x / y


@time_it
def add(x, y):
    return x + y


@time_it
def sub(x, y):
    return x - y


@time_it
def mul(x, y):
    return x * y


@time_it
def square(x):
    """
    This function returns the square of x.
    :param x:
    :return:
    """
    return x ** 2

# print(dir(square))
# print(square.__code__)
help(square)

#
# x = time_it
#
# print(x.__name__)


square(5)
add(10, 10)
add(10, 20)
add(x=10, y=30)
sub(10, 10)
div(10, 10)
# decorated_div = time_it(div)
#
# decorated_div
#
# div
# div = time_it(div)

# print(div(20, 2))


#
# def func():
#     def inner():
#         pass
#     return inner


# def func(f):
#     return f


# blabla = func(add)
# print(blabla(10, 2))
# print(div(10, 2))
