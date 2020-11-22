num = input('Enter a number: ')

result = 1

for digit in num:
    if digit != '0':
        result = result * int(digit)

print(result)

num = int(input('Enter a number: '))

result = 1

while num != 0:
    digit = num % 10
    if digit != 0:
        result = result * digit
        # result *= digit
    num = num // 10

print(result)

num = int(input('Enter a number: '))

result = 1

while True:
    digit = num % 10
    if digit != 0:
        result = result * digit
        # result *= digit
    num = num // 10

    if num == 0:
        break

print(result)
