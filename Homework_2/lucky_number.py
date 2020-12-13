def is_lucky(value):
    odd_even = 0
    even_sum = 0

    is_odd = True

    while value > 0:
        last_digit = value % 10
        if is_odd:
            odd_even += last_digit
        else:
            even_sum += last_digit

        is_odd = not is_odd
        value //= 10

    return odd_even == even_sum


# def is_lucky(value):
#     odd_sum = 0
#
#     for digit in value[0::2]:
#         odd_sum += int(digit)
#
#     even_sum = 0
#
#     for digit in value[1::2]:
#         even_sum += int(digit)
#
#     return odd_sum == even_sum

    # lucky_sum = 0
    #
    # for i in range(len(value)):
    #     if i % 2 == 0:
    #         lucky_sum += int(value[i])
    #     else:
    #         lucky_sum -= int(value[i])
    #
    # return lucky_sum == 0


num = int(input('Enter a number: '))

if is_lucky(num):
    print('Yes')
else:
    print('No')
