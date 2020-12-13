def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def perimeter(values):
    a = distance(values[0], values[1], values[2], values[3])
    b = distance(values[2], values[3], values[4], values[5])
    c = distance(values[4], values[5], values[6], values[7])
    d = distance(values[6], values[7], values[0], values[1])

    return a + b + c + d


coords = [float(i) for i in input('Enter a sequence: ').split()]
print(perimeter(coords))
