# Introduction to Generator functions in Python
import os
os.system('cls')

def generator_1(n=0):
    yield 1
    print('Continuing...')
    yield 2
    print('One more...')
    yield 3
    print('Now it is finished...')
    return 'FINISHED'

gen_1 = generator_1()
for n in gen_1:
    print(n)

def generator_2(n=0, maximum=10):
    while True:
        yield n
        n += 2
        if n >= maximum:
            return

gen_2 = generator_2(n=2, maximum=8)
for n in gen_2:
    print(n)
    