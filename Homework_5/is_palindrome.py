def is_palindrome_v2(text, i=0):
    print(id(text))
    if len(text) <= 1 or i == len(text) // 2:
        return True

    if text[i] == text[-i-1]:
        return is_palindrome_v2(text, i + 1)

    return False


def is_palindrome(text):
    # if len(text) == 0 or len(text) == 1:
    print(id(text))
    if len(text) <= 1:
        return True

    if text[0] == text[-1]:
        return is_palindrome(text[1: -1])

    return False


if is_palindrome_v2(input('Enter a text: ')):
    print('Yes')
else:
    print('No')
