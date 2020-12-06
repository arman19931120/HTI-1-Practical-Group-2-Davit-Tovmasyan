def digit_sum(value):
    _digit_sum = 0

    while value != 0:
        _digit_sum += value % 10
        value //= 10

    return _digit_sum


def number_root(num):
    while num > 9:
        num = digit_sum(num)

    return num


number = int(input('Enter a number: '))
root = number_root(number)
print(root)
