import json
import os
from exercise_01a import PATH, Person, dump_file

os.system('cls')

with open(PATH, 'r') as file:
    data_people = json.load(file)

    p1 = Person(**data_people[0])
    p2 = Person(**data_people[1])
    p3 = Person(**data_people[2])
    p4 = Person(**data_people[3])

print(p1.__dict__)
print(p2.__dict__)
print(p3.__dict__)
print(p4.__dict__)