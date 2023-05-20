# Introduction to Python Functions - def defines a function
import os
os.system('cls')

def print_out(a, b, c):
    print(a, b, c)

print_out(1,2,3)
print_out(4,5,6)

def say_hello(name='no name'):
    print(f'Olá, {name}')

say_hello('Gabriel')
say_hello()

# Named Arguments and Positional (Unnamed) Arguments in Functions
os.system('cls')

def sum(x,y):
    print(f'{x=} {y=} | x + y = {x + y}')

sum(1, 2)
sum(2, 1)
sum(y=2, x=1)

# Default values for parameters in Python functions + NoneType and None
os.system('cls')

def sum_2(x, y, z=None):
    if z is not None:
        print(f'{x=} {y=} {z=}| x + y + z = {x + y + z}')
    else:
        print(f'{x=} {y=} | x + y = {x + y}')

sum_2(1, 2)
sum_2(1, 2, 3)

# Return of function values
os.system('cls')

def division(x, y):
    if y == 0:
        return 0
    return x / y

division_1 = division(10, 2)
print(division_1)

division_1 = division(10, 0)
print(division_1)

# *args for number of unnamed variable arguments
os.system('cls')

def sum_args(*args):
    result = 0
    for number in args:
        result += number
    return result

sum_args = sum_args(1,2,3,4,5,6)
print(sum_args)

# Higher Order Functions
os.system('cls')

def say_the_mensagem(mensagem, name):
    return f'{mensagem}, {name}'

def execute_the_function(function, *args):
    return function(*args)

variable = execute_the_function(say_the_mensagem, 'Hello world', 'Gabriel')

print(variable)

# Closure and functions that return other functions
os.system('cls')

def create_salutation(salutation):
    def say_salutation(name):
        return f'{salutation}, {name}!'
    return say_salutation

say_good_morning = create_salutation('Good morning')
say_good_afternoon = create_salutation('Good afternoon')

for name in ['Maria', 'João', 'Ana']:
    print(say_good_morning(name))

for name in ['Maria', 'João', 'Ana']:
    print(say_good_afternoon(name))
