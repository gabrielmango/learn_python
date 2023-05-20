import os
os.system('cls')

def multiply_args(*args):
    result = 1
    for number in args:
        result *= number
    return result

multiply_1 = multiply_args(2,3,4)
print(multiply_1)

def even_or_odd(number):
    if number % 2 == 0:
        return f'{number} is even!'
    return f'{number} is odd!'
    
print(even_or_odd(2))
print(even_or_odd(3))

def is_even(number):
    return number % 2 == 0

print(is_even(2))
print(is_even(3))