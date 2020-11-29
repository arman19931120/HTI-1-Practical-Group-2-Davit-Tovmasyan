year = int(input('Enter a year: '))

century = year // 100

if year % 100 != 0:
    century += 1

print(century)
