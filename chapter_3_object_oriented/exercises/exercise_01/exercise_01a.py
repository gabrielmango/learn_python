import json
import os

os.system('cls')

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person('Gabriel', 28)
p2 = Person('Henrique', 25)
p3 = Person('Mateus', 21)
p4 = Person('Lucas', 32)

data_people = [vars(p1), vars(p2), vars(p3), vars(p4)]
# print(data_people)

PATH = r'C:\\github_gabrielmango\\learn_python\\chapter_3_object_oriented\\exercises\\exercise_01\\exercise_01.json'

def dump_file():
    with open(PATH, 'w', encoding='utf8') as file:
        json.dump(data_people, file, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    dump_file()