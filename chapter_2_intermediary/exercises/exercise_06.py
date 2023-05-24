import os
from itertools import zip_longest
os.system('cls')


list_1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
list_2 = ['BA', 'SP', 'MG', 'RJ']

print(list(zip(list_1, list_2)))
print(list(zip_longest(list_1, list_2, fillvalue='No city')))