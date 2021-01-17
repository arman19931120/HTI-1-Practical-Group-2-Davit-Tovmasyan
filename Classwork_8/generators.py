# def my_range(*args):  # [start, stop)
#     if len(args) == 1:
#         start, stop, step = 0, args[0], 1
#     elif len(args) == 2:
#         start, stop, step = args[0], args[1], 1
#     elif len(args) == 3:
#         start, stop, step = args[0], args[1], args[2]
#     else:
#         raise TypeError('We expect 1, 2 or 3 arguments.')
#
#     current = start
#
#     while current < stop:
#         yield current
#         current += step
#
#
# for i in my_range(10):
#     print(i)


# def my_enumerate(items):
#     result = []
#
#     for i in range(len(items)):
#         result.append((i, items[i]))
#
#     return result
#
# def my_enumerate(items):
#     for i in range(len(items)):
#         yield i, items[i]


# sum_of = 0
# for i in map(lambda x: x ** 2, [1, 2, 3, 4, 5]):
#     sum_of += i
#



# print(list(my_enumerate([1, 2, 3])))
#
# for i, num in my_enumerate([1, 4, 5, 6, 7]):
#     print(i, num)
#
# for i, num in my_enumerate([1, 4, 5, 6, 7]):
#     print(i, num)


# for i in range(len(numbers)):
#     numbers[i]

# print(list(enumerate([1, 2, 3, 4])))
#
# for i, num in [(0, 1), (1, 2), (2, 3), (3, 4)]:
#     print(i, num)

# for i, num in enumerate([1, 2, 3, 4]):
#     print(i, num)



# numbers = (i * i for i in range(10000))

#
# for num in numbers:
#     print(num)
#     break
#
# for num in numbers:
#     print(num)
#     break


# for i in range(100000000000000000000):  # [0, 1, 2, 3, 4, 5...100000000000000000000-1]
#     print(i)
#
# import sys
#
#
# if __name__ == '__main__':
#     print(sys.argv)
#
#     print(list(my_gen()))
#
