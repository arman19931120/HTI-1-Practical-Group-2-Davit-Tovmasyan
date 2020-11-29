def is_prime(number):
    _is_prime = True

    for i in range(2, number // 2 + 1):
        if number % i != 0:
            _is_prime = False
            break

    return _is_prime


num = int(input('Enter a number: '))

if is_prime(num):
    print('Yes')
else:
    print('No')
