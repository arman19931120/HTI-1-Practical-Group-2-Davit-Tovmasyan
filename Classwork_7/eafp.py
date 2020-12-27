# LBYL
#
# import os
#
# my_file = "/path/to/my/file.txt"
#
# # Race condition
# if os.access(my_file, os.R_OK):
#     with open(my_file) as f:
#         print(f.read())
# else:
#     print("File can't be accessed")
#
#
# # EAFP
# # No race condition
# try:
#     f = open(my_file)
# except IOError as e:
#     print("File can't be accessed")
# else:
#     with f:
#         print(f.read())

def square_add(x, y):
    if isinstance(x, int) and isinstance(y, int):
        return x ** 2 + y ** 2

    print('Unable to work with non integers.')


def square_add_eafp(x, y):
    try:
        return x ** 2 + y ** 2
    except TypeError:
        print('Unable to work with non integers.')


print(square_add(2, 3))
print(square_add(2.5, 3.5))
print(square_add(2.5, 3))
print(square_add('lol', '90'))



# import os
# import sys
#
#
# def make_a_dir(path, directory):
#     initial_path = os.getcwd()
#     os.chdir(path)
#     try:
#         os.makedirs(directory)
#     finally:
#         os.chdir(initial_path)
#
#
# if __name__ == '__main__':
#     try:
#         make_a_dir(sys.argv[1], sys.argv[2])
#     except FileNotFoundError:
#         pass
#
