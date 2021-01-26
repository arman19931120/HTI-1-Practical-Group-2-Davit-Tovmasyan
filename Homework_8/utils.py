def has_only_odd(num):
    result = True

    while num != 0:
        if (num % 10) % 2 == 0:
            result = False
            break

        num //= 10

    return result


def has_only_even(num):
    result = True

    while num != 0:
        if (num % 10) % 2 == 1:
            result = False
            break

        num //= 10

    return result


def is_prime(num):
    result = True

    for i in range(2, num // 2 + 1):
        if num % i == 0:
            result = False
            break

    return result



def numbers(start, stop, filter_function):
    while start < stop:
        if filter_function(start):
            yield start
        start += 1


# print(list(numbers(100, 200, filter_function=has_only_odd)))
# print(list(numbers(200, 400, filter_function=has_only_even)))
# print(list(numbers(0, 100, filter_function=is_prime)))
# print(list(numbers(0, 10, filter_function=lambda x: x % 2 == 0)))


def my_map(func, values):
    for item in values:
        yield func(item)


print(list(my_map(int, '1278973')))

def my_zip(*lists):
    i = 0
    length = min(len(l) for l in lists)
    while i < length:
        yield [l[i] for l in lists]
        i += 1


def my_filter(func, values):
    for i in values:
        if func(i):
            yield i

# filter(lambda x: x < 10, [1, 10, 12, 12, 3, 55])


# def my_filter(func, values):
#     for item in values:
#         yield func(item)
