# Free variables + nonlocal (locals, globals)
import os
os.system('cls')

def concatenate_strings(first_string):
    final_string = first_string

    def internal_function(value_to_concatenate=''):
        nonlocal final_string
        final_string += value_to_concatenate
        return final_string

    return internal_function

c = concatenate_strings('a')
print(c('b'))
print(c('c'))
print(c('d'))

final = c()

print(final)

# Decorator functions in general
os.system('cls')

def create_func(func):
    def internal_function(*args, **kwargs):
        for arg in args:
            is_string(arg)
        result = func(*args, **kwargs)
        return result
    return internal_function

@create_func
def inverte_string(string):
    return string[::-1]

def is_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')

invertida = inverte_string('123')
print(invertida)

# Decorators with parameters
os.system('cls')

def factory_of_decorators(a=None, b=None, c=None):
    def factory_of_functions(function):
        def internal_function(*args, **kwargs):
            result = function(*args, **kwargs)
            return result
        return internal_function
    return factory_of_functions

@factory_of_decorators
def sum(x, y):
    return x + y

multiply = factory_of_decorators()(lambda x,y: x * y)
ten_times_two = multiply(10, 2)
print(ten_times_two)

# Order of application of decorators
os.system('cls')
def decorator_parameters(name):
    def decorator(func):
        print('decorator:', name)

        def new_function(*args, **kwargs):
            result = func(*args, **kwargs)
            final = f'{result} {name}'
            return final
        return new_function
    return decorator


@decorator_parameters(name='5')
@decorator_parameters(name='4')
@decorator_parameters(name='3')
@decorator_parameters(name='2')
@decorator_parameters(name='1')
def soma(x, y):
    return x + y


ten_plus_five = soma(10, 5)
print(ten_plus_five)