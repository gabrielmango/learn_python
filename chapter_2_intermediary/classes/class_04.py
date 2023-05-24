# Introduction to lambda function + list.sort and sorted
import os
os.system('cls')

def display_list(list):
    for item in list:
        print(item)
    print()

list_of_names = [
    {'name': 'Luiz', 'last_name': 'miranda'},
    {'name': 'Maria', 'last_name': 'Oliveira'},
    {'name': 'Daniel', 'last_name': 'Silva'},
    {'name': 'Eduardo', 'last_name': 'Moreira'},
    {'name': 'Aline', 'last_name': 'Souza'},
]

list_of_names.sort(key=lambda item: item['name'])

list_order_names = sorted(list_of_names, key=lambda item: item['name'])
list_order_last_names = sorted(list_of_names, key=lambda item: item['last_name'])

display_list(list_order_names)
display_list(list_order_last_names)

# Complex lambda functions (for understanding)
os.system('cls')

def execute_function(function, *args):
    return function(*args)

def sum(x, y):
    return x + y

print(execute_function(lambda x, y: x + y, 1, 1))

def create_multiplier(multiplier):
    def multiply(number):
        return multiplier * number
    return multiply

duplicate = execute_function(lambda m: lambda n: m * n, 2)
print(duplicate(2))

# Packing and unpacking dictionaries
os.system('cls')

person = {
    'first_name': 'Gabriel',
    'last_name': 'Mango',
}

data_person = {
    'age': 28,
    'height_in_meters': 1.78,
}

person_complited = {**person, **data_person}
print(person_complited)