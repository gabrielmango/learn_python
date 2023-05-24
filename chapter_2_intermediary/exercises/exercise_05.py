import os
import copy

os.system('cls')

increase_price = 1.10

products = [
    {'name': 'product 5', 'price': 10.00},
    {'name': 'product 1', 'price': 22.32},
    {'name': 'product 3', 'price': 10.11},
    {'name': 'product 2', 'price': 105.87},
    {'name': 'product 4', 'price': 69.90},
]

new_products_1 = [
    {**product, 'price' : round(product['price'] * increase_price, 2)}
    for product in copy.deepcopy(products)
]

products_sorted_by_name = sorted(
    copy.deepcopy(products),
    key=lambda p: p['name'],
    reverse= True
)

products_sorted_by_price = sorted(
    copy.deepcopy(products),
    key=lambda p: p['price'],
)

print(*products, sep='\n')
print()
print(*products_sorted_by_name, sep='\n')
print()
print(*products_sorted_by_price, sep='\n')


