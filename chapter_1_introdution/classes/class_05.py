# # Type list - Introduction to mutable lists in Python

import os
os.system('cls')

list_1 = [123, True, 'Gabriel', 1.6]
print(list_1)
print(type(list_1))

for item in list_1:
    print(item)
    print(type(item))


os.system('cls')
list_1 = [1,2,3,4,5,6,7,8,9]
print(list_1)
list_1.append(10)
list_1.append(11)
print(list_1)
list_1.pop()
print(list_1)
last_value = list_1.pop()
print(list_1)
print('Last value: ', last_value)


os.system('cls')
list_1 = [10,20,30,40,50,60,70,80,90]
list_1.insert(0, 'First value')
print(list_1)


os.system('cls')
list_a = [1,2,3]
list_b = [4,5,6]
list_c = list_a + list_b
list_a.extend(list_b)
print(list_c)
print(list_a)


os.system('cls')
names = ['Maria', 'Júlia', 'Ana']
name_1, name_2, name_3 = names
print(names)
print(name_1)
print(name_2)
print(name_3)
nome4, *another_names = ['Ana', 'Paula', 'João']
print(nome4, another_names)


os.system('cls')
names = ('Maria', 'Júlia', 'Ana')
print(names, type(names))


sentence = 'look at that, interesting thing'
print(sentence)
words_list_1 = sentence.split()
print(words_list_1)
sentence_2 = 'look at that, interesting thing'
words_list_2 = sentence.split(',')
print(words_list_2)
sentence_3 = 'look at that, interesting thing'
words_list_3 = sentence.split(',')
sentence_list_fixed = []
for i, sentence in enumerate(words_list_3):
    sentence_list_fixed.append(words_list_3[i].strip())
print(sentence_list_fixed)
unided_sentences = '-'.join(sentence_list_fixed)
print(unided_sentences)


classrooms = [
    ['Maria', 'Helena'],
    ['Elaine'],
    ['Luiz', 'João', 'Eduarda',],   
]
print(classrooms)
for classroom in classrooms:
    for student in classroom:
        print(student)

