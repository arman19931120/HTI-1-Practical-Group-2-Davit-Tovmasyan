import re
import sys


def validate_phone_number(phone_number):
    expression = (
        '0?(77|55|99|91|98)[ -]?'
        '('
            r'(\d{3}[ -]?\d{3})|'
            r'((\d{2} ){2}\d{2})|'
            r'((\d{2}-){2}\d{2})'
        ')'
    )

    return re.fullmatch(expression, phone_number) is not None


def validate_email(email):
    expression = r'\w{1}(\.?[\_\-\+\w])*@\w{1}[\.\-\+\w]*(\.[a-z]{2,5})'

    return re.fullmatch(expression, email) is not None


if __name__ == '__main__':
    commands = {
        'email': validate_email,
        'phone_number': validate_phone_number,
    }

    if len(sys.argv) == 1:
        print('Type one of the following commands.\nemail\nphone_number')
    elif len(sys.argv) == 2:
        print('No value passed.')
    elif len(sys.argv) == 3:
        command = sys.argv[1]
        value = sys.argv[2]

        if command not in commands:
            print('No such command.')
        else:
            func = commands[command]
            if func(value):
                print('Yes')
            else:
                print('No')

        # if sys.argv[1] == 'email':
        #     if validate_email(sys.argv[2]):
        #         print('Yes')
        #     else:
        #         print('No')
        # elif sys.argv[1] == 'phone_number':
        #     if validate_phone_number(sys.argv[2]):
        #         print('Yes')
        #     else:
        #         print('No')
        # else:
        #     print('No such command.')

        
