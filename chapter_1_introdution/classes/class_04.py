
# while and break - Repetition structure

while True:
    name = input('What is your name: ')
    if name == 'leave':
        print('You left.')
        break
    print(f'Your name is {name}.')
print('Finished.')

counter = 0
while counter < 10:
    counter += 1
    if counter == 6:
        print('I will not show the value 6')
        continue
    print(counter)


string = 'Some value'
i = 0
while i < len(string):
    letter = string[i]
    print(letter)
    i += 1
else:
    print('The else has been executed.')
print('Fora do while.')


# Introduction to for/in - looping structure for finite things

text = 'Python'
for letter in text:
    print(letter)


numbers = range(0, 10, 1)
for number in numbers:
    print(number)


for i in range(10):
    if i == 2:
        print('i is 2, jumping...')
        continue
    if i == 8:
        print('i is 8, your else will not execute.')
        break
    for j in range(1, 3):
        print(i, j)
else:
    print('Completed successfully!')

