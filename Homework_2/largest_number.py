def is_largest(value):
    is_large = True

    while value > 9:
        a, b = value // 10 % 10, value % 10
        if b > a:
            is_large = False
            break

        value //= 10

    return is_large


number = int(input('Enter a number: '))
if is_largest(number):
    print('Yes')
else:
    print('No')
