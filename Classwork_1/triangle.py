a = int(input('Enter a number: '))
b = int(input('Enter a number: '))
c = int(input('Enter a number: '))

# sides = [a, b, c]
# sides = [5, 4, 3]
# sides.sort()
# sides = [3, 4, 5]
#
# a = sides[0]
# b = sides[1]
# c = sides[2]

if a >= b and a >= c:
    # temp = c
    # c = a
    # a = temp
    a, c = c, a
elif b >= a and b >= c:
    b, c = c, b

if c >= a + b:
    print('Not a triangle')
elif c * c == a * a + b * b:
    print('Right triangle')
elif c * c < a * a + b * b:
    print('Acute triangle')
else:
    print('Obtuse triangle')
