# # Introduction to code blocks + if / elif / else (conditionals)

import os
os.system('cls')

entry_1 = input("Do you want to 'enter' or 'leave'?")
if entry_1 == 'enter':
    print('You have entered the system.')
elif entry_1 == 'leave':
    print('You have logged out of the system.')
else:
    print('Invalid answer.')  


condition = True
if condition:
    print('This is the if code block.')
else:
    print('This is the code block for else.')
if 10 == 10:
    print('Another if')


entry_2 = input('[E]nter or [L]eave: ')
entered_password = input('Password: ')
allowed_password = '123456'
if entry_2 == 'E' and entered_password == allowed_password:
    print('To enter.')
else:
    print('To go out.')



entry_3 = input('[E]nter or [L]eave: ')
allowed_password = '123456'
if entry_3 == 'E' or entry_3 == 'e':
    print('To enter.')

password = input('Enter : ') or 'no password'
print(password)



password = input('Enter a password: ')
if not password:
    print('You did not enter the password!')
elif password == '123456':
    print('Password correct!')
else:
    print('Incorrect password!')



name = input('Enter your name: ')
find_letters = input('Which letter do you want to find?')
if find_letters in name:
    print(f'"{find_letters}" is in "{name}"')
else:
    print(f'"{find_letters}" is not in "{name}"')


name = 'Gabriel'
price = 1000.9513465
message = '%s, the price is R$%.2f! ' % (name, price)


print(10 * '-')
print(message)
print(10 * '-')


variable = 'ABC'
value = 1000.68137
integer = 1500

print(f'{variable}.')
print(f'{variable: >15}.')
print(f'{variable: <15}.')
print(f'{variable: ^15}.')
print(f'{value:0=+10,.1f}.')
print(f'{integer:08x}.')


# Ternary operation with Python (one-line if and else)

condition = False
variable = 'Value' if condition else 'Another value'
print(variable)

