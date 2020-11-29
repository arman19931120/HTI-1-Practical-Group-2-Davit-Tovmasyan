a1 = int(input('Enter the first number: '))
a2 = int(input('Enter the second number: '))

n = int(input('Enter the position: '))

delta = a2 - a1

a_n = a1 + (n - 1) * delta

print(f'[{n}] = {a_n}')
