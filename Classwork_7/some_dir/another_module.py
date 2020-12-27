def is_palindrome(text):
    if len(text) <= 1:
        return True

    if text[0] == text[-1]:
        return is_palindrome(text[1: -1])

    return False


if __name__ == '__main__':
    if is_palindrome(input('Enter a text: ')):
        print('Yes')
    else:
        print('No')
