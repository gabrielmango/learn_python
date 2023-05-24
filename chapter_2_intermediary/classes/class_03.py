# Introduction to the set type in Python (sets)
import os
os.system('cls')

s1 = set('gabriel')
print(s1, type(s1))

s2 = {'Gabriel'}
print(s2, type(s2))

# Peculiarities of the set mutable type in Python
os.system('cls')

list_1 = [1,2,3,1,2,3,1,2,3]
set_1 = set(list_1)
upgraded_list_1 = list(set_1)
print(list_1)
print(upgraded_list_1)

# Useful methods of type set in Python
os.system('cls')

set_2 = set()
set_2.add('Gabriel')
set_2.add(1)
print(set_2)

set_2.update(('Hello World!',))
print(set_2)

set_2.discard(('Hello Wordl!',))
print(set_2)

set_2.clear()
print(set_2)

# Important operators for the set type (sets)
os.system('cls')

set_3 = {1,2,3}
set_4 = {2,3,4}

print(f'Union: {set_3 | set_4}')
print(f'Intersection: {set_3 & set_4}')
print(f'Difference: {set_3 - set_4}')
print(f'Difference: {set_4 - set_3}')
print(f'Symmetric difference: {set_3 ^ set_4}')

# Example of using the set type
os.system('cls')

letters = set()
while True:
    letter = input('Enter a letter: ')
    letters.add(letter.lower())

    if 'l' in letters:
        print('Finished!')
        break

    print(letters)