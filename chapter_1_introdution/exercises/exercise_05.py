import os
os.system('cls')

name = input('Enter your name: ')

i = 0
new_name = ''

while i < len(name):
    new_name += f'*{name[i]}'
    i += 1

new_name += '*'
print(new_name)
