def missing_number(values):
    n = len(values) + 1

    return n * (n + 1) // 2 - sum(values)


numbers = [int(i) for i in input('Enter a sequence: ').split()]
print(missing_number(numbers))
