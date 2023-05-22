# Introduction to List comprehension in Python
import os
os.system('cls')

list_1 = [
    number * 2
    for number in range(10)
]

print(list_1)

# Data mapping in list comprehension (map)
os.system('cls')

products = [
    {'name': 'p1', 'price': 20, },
    {'name': 'p2', 'price': 10, },
    {'name': 'p3', 'price': 30, },
]

new_products = [
    product
    for product in products
]

print(*new_products, sep='\n')

# Data filter in list comprehension (filter)
import pprint
os.system('cls')

def p(a):
    pprint.pprint(a, sort_dicts=False, width=40)

list_2 = [n for n in range(10) if n < 5]
p(list_2)

# List comprehension with more than one for
os.system('cls')

list_3 = []
for x in range(3):
    for y in range(3):
        list_3.append((x, y))
print(list_3)

list_4 = [
    (x, y)
    for x in range(3)
    for y in range(3)
]
print(list_4)

# Dictionary Comprehension and Set Comprehension
os.system('cls')

product = {
    'name': 'blue pen',
    'price': 2.5,
    'category': 'office'
}

new_product = {
    key: value.upper()
    if isinstance(value, str) else value
    for key, value in product.items()
    if key != 'category'
}
print(product)
print(new_product)

set_1 = {i ** 2 for i in range(10)}
print(set_1)

# isinstance() - to find out if the object is of a certain type
os.system('cls')

list_a = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2),
    {0, 1}, {'nome': 'Luiz'},
]
print(list_a)

for item in list_a:
    if isinstance(item, set):
        item.add(5)
        print(item)
    elif isinstance(item, str):
        print(item.upper())
    elif isinstance(item, (int, float)):
        print(item, item * 2)
    else:
        ...

# Truthy and Falsy Values, Mutable and Immutable Types
os.system('cls')

lista = []
dicionario = {}
conjunto = set()
tupla = ()
string = ''
inteito = 0
flutuante = 0.0
nada = None
falso = False
intervalo = range(0)

list_of_types = [
    lista, dicionario, conjunto, 
    tupla, string, inteito, 
    flutuante, nada, falso, intervalo]

def falsy(valor):
    return 'falsy'if not valor else 'truthy'

for value in list_of_types:
    print(falsy(value))

# dir, hasattr and getattr in Python
os.system('cls')

name = 'Gabriel'
method = 'upper'

methods_name = dir(name)
for item in methods_name:
    if 'center' in item:
        print(item)

if hasattr(name, method):
    print(f'There is the method {method}')
    print(getattr(name, method)())
else:
    print(f'There is not the method {method}')

# Generator expression, Iterables and Iterators in Python
import sys
os.system('cls')

list_b = [n for n in range(10000)]
generated = (n for n in range(10000))

print(sys.getsizeof(list_b))
print(sys.getsizeof(generated))