import os
os.system('cls')

name = input('enter your name: ')
age = input('enter your age: ')


if name and age:
    print(f'Your name is {name}')
    print(f'Your inverted name is "{name[::-1]}"')
    if ' ' in name:
        print('Your name contains spaces.')
    else:
        print('Your name does not contain spaces.')
    print(f'Your name has {len(name)} letters.')
    print(f'The first letter of your name is "{name[0]}"')
    print(f'The last letter of your name is "{name[len(name) - 1]}"')
else:
    print('Sorry, you left fields empty.')
