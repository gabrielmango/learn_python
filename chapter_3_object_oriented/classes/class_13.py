from dataclasses import dataclass, asdict, astuple

@dataclass
class Person:
    name: str
    last_name: str
    age: int

    @property
    def full_name(self):
        return f'{self.name} {self.last_name}'

    @full_name.setter
    def full_name(self, value: str):
        name, *last_name = value.split()
        self.name = name
        self.last_name = ' '.join(last_name)


if __name__ == '__main__':
    person_1 = Person('Gabriel', 'Mango', 28)

    print(person_1)
    
    person_1.full_name = 'Gabriel Henrique Mango'
    person_1.age = 32

    print(person_1)
    print(astuple(person_1))
    print(asdict(person_1))