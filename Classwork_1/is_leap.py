year = int(input('Enter a year: '))

# Եթե տարեթիվը չի բաժանվում 4 - ի, ապա այն հասարակ է։
# Եթե տարեթիվը բաժանվում է 4 - ի և չի բաժանվում 100 - ի, ապա այն նահանջ է։
# Եթե տարեթիվը բաժանվում է 4 - ի, 100 - ի և 400 - ի, ապա այն նահանջ է։
# Մնացած բոլոր դեպքերում այն հասարակ է։


if year % 4 != 0:
    print('No')
elif year % 100 != 0:
    print('Yes')
elif year % 400 == 0:
    print('Yes')
else:
    print('No')
