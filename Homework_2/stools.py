def stools(values):
    max_height = max(values)

    height_of_stools = 0

    for height in values:
        height_of_stools += max_height * height

    return height_of_stools


heights = [int(i) for i in input('Enter a sequence: ').split()]
print(stools(heights))
