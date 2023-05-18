import os
os.system('cls')

number = input('Enter a number: ')

try:
    if int(number) % 2 == 0:
        print(f'The number "{number}" is even.')
    else:
        print(f'The number "{number}" is odd.')
except:
    print('It is not a integer number')
    