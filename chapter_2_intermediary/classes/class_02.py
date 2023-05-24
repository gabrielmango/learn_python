### Introduction to the dict data type - Python Dictionaries
import os
os.system('cls')

person_2 = dict(first_name='Mateus', last_name='da Costa', age=25)

person_1 = {
    'first_name': 'Gabriel',
    'last_name': 'Mango',
    'age': 27,
    'height_in_meeters': 1.78,
    'adresses': [
        {'street': 'One', 'number': 159},
        {'street': 'Two', 'number': 187},
    ]
}

for key in person_1:
    print(f'{key}: {person_1[key]}')

# Manipulating Keys and Values in Python Dictionaries
os.system('cls')

person_3 = {}

key_1 = 'full_name'
person_3[key_1] = 'Ana Maria da Costa'
print(person_3)

key_2 = 'age'
person_3[key_2] = 42
print(person_3)

del person_3[key_2]
print(person_3)

if person_3.get(key_2) is None:
    print('There is not age')
else: 
    print(person_3[key_2])

# Shallow Copy vs Deep Copy on Python mutable data
import copy
os.system('cls')

dictionary_1 = {
    'key1': 1,
    'key2': 2,
    'list': [1,2,3]
}

dictionary_2 = dictionary_1.copy()
dictionary_3 = copy.copy(dictionary_1)
dictionary_4 = copy.deepcopy(dictionary_1)

dictionary_1['key1'] = 9999999
dictionary_1['list'][1] = 999999

print(dictionary_1)
print(dictionary_2)
print(dictionary_3)
print(dictionary_4)


