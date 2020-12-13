def is_prime(value):
    _is_prime = True

    for i in range(2, value // 2 + 1):
        if value % i == 0:
            _is_prime = False
            break

    return _is_prime


def goldbach(value):
    for i in range(2, value):
        if is_prime(i) and is_prime(value - i):
            return i, value - i


num = int(input('Enter a number: '))

prime1, prime2 = goldbach(num)

print(prime1, prime2)
