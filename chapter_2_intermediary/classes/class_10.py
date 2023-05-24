import json
import os
os.system('cls')
person = {
    'name': 'Gabriel',
    'last_name': 'Mango',
    'address': [
        {'street': 'R1', 'number': 25},
        {'street': 'R2', 'number': 75},
    ],
    'height_in_meters': 1.78,
    'preferred_numbers': [1,2,3,4,5,6],
    'Dev': True,
    'anything': None,
}


path = r'C:\\github_gabrielmango\\learn_python\\chapter_2_intermediary\\classes\\class_10.json'

with open(path, 'w', encoding='utf8') as file:
    json.dump(person, file, indent=2)


with open(path, 'r', encoding='utf8') as file:
    person_2 = json.load(file)
    print(person_2['name'])

os.remove(path)