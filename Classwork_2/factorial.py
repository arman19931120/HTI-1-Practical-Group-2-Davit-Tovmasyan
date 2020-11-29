def factorial(number):
    result = 1

    for i in range(2, number + 1):
        result *= i

    return result


num = int(input('Enter a number: '))
print(factorial(num))
