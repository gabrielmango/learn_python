# Count is an endless iterator (itertools)
import os
from itertools import count
os.system('cls')

c1 = count(8, 8)
r1 = range(8, 100, 8)

print('c1', hasattr(c1, '__iter__'))
print('c1', hasattr(c1, '__next__'))
print()
print('r1', hasattr(r1, '__iter__'))
print('r1', hasattr(r1, '__next__'))

print(c1)
for i in c1:
    if i >= 100:
        break
    print(i)

print(r1)
for i in r1:
    print(i)

# Combinations, Permutations and Product - Itertools
from itertools import combinations, permutations, product
os.system('cls')

def print_inter(iterator):
    internal_list = list(iterator)
    print(*internal_list, sep='\n')
    print()

def print_len_iter(iterator):
    internal_list = list(iterator)
    print(len(internal_list))
    print()

people = ['João', 'Joana', 'Luiz', 'Letícia',]

t_shirts = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['masculino', 'feminino', 'unisex'],
    ['algodão', 'poliéster']
]

print_inter(combinations(people, 2))
print_inter(permutations(people, 2))
print_inter(product(*t_shirts))
print_len_iter(product(*t_shirts))

# groupby - grouping values (itertools)
from itertools import groupby
os.system('cls')

students = [
    {'name': 'Luiz', 'grade': 'A'},
    {'name': 'Letícia', 'grade': 'B'},
    {'name': 'Fabrício', 'grade': 'A'},
    {'name': 'Rosemary', 'grade': 'C'},
    {'name': 'Joana', 'grade': 'D'},
    {'name': 'João', 'grade': 'A'},
    {'name': 'Eduardo', 'grade': 'B'},
    {'name': 'André', 'grade': 'A'},
    {'name': 'Anderson', 'grade': 'C'},
]

def order_by_grade(students):
    return students['grade']

def order_by_name(students):
    return students['name']

students_groupby = sorted(students, key=order_by_grade)
groups = groupby(students_groupby, key=order_by_grade)

for key, group in groups:
    print(key)
    for studenty in group:
        print(studenty)

# map, partial, GeneratorType and exhaustion of Iterators
from functools import partial
from types import GeneratorType
os.system('cls')

products = [
    {'name': 'Produto 5', 'price': 10.00},
    {'name': 'Produto 1', 'price': 22.32},
    {'name': 'Produto 3', 'price': 10.11},
    {'name': 'Produto 2', 'price': 105.87},
    {'name': 'Produto 4', 'price': 69.90},
]

def increase_percentage(value, percentage):
    return round(value * percentage, 2)

increase_ten_percent = partial(increase_percentage, percentage=1.1)

def change_price_of_products(product):
    return {**product, 'price': increase_ten_percent(product['price'])}

new_products = map(change_price_of_products, products)

print_inter(products)
print_inter(new_products)

# filter is a functional filter
os.system('cls')

def filter_price(product):
    return product['price'] > 100

filtered_products_1 = filter(lambda p: p['price'] > 100, products)
filtered_products_2 = filter(filter_price, products)
print_inter(filtered_products_1)
print_inter(filtered_products_2)

# reduce - reduces an iterable to a value
from functools import reduce
os.system('cls')

total_prices = round(reduce(
    lambda acumulador, product: acumulador + product['price'], 
    products, 
    0), 2)

print('total prices: ', total_prices)
print('total prices: ', round(sum([p['price'] for p in products]), 2))