num = input('Enter a number: ')

half = len(num) // 2
num = int(num)

diff = 0
i = 0

while num > 0:
    if i < half:
        diff += num % 10
    else:
        diff -= num % 10

    num //= 10
    i += 1

if diff == 0:
    print('Yes')
else:
    print('No')
