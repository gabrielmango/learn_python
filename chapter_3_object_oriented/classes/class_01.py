# Introduction to Classes
import os
os.system('cls')

class Person():
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name

p1 = Person('Gabriel', 'Mango')
p2 = Person('Mateus', 'da Costa')

print(p1.name, p1.last_name)
print(p2.name, p2.last_name)

# Methods on instances of Python classes
os.system('cls')

class Car():
    def __init__(self, name):
        self.name = name

    def speed_up(self):
        print(f'{self.name} is accelerating!')

fusca = Car('fusca')
fusca.speed_up()
Car.speed_up(fusca)
print()
celta = Car('celta')
celta.speed_up()
Car.speed_up(celta)

# Class scope and class methods
os.system('cls')

class Animal:
    def __init__(self, name):
        self.name = name

        value = 'value'
        print(value)
    
    def eating(self, food):
        return f'{self.name} is eating {food}'
    
    def execute(self, *args, **kwargs):
        return self.eating(*args, **kwargs)
    
lion = Animal(name='Lion')
print(lion.name)
print(lion.execute('apple'))

# Keeping states inside the class
os.system('cls')

class Camera:
    def __init__(self, name, shooting=False) -> None:
        self.name = name
        self.shooting = shooting
    
    def film(self):
        if self.shooting:
            print(f'{self.name} is already filming!')
            return
        print(f'{self.name} is filming!')
        self.shooting = True

    def stop_filming(self):
        if not self.shooting:
            print(f'{self.name} is not already filming!')
            return
        print(f'{self.name} is stopping filming!')
        self.shooting = False
    
    def photograph(self):
        if self.shooting:
            print(f'{self.name} can not take pictures while filming!')
            return 
        print(f'{self.name} is photographing now!')

c1 = Camera('Canon')
c2 = Camera('Sony')

c1.film()
c1.film()
c1.photograph()
c1.stop_filming()
c1.photograph()
print()
c2.stop_filming()
c2.film()
c2.photograph()
c2.film()
c2.photograph()

# class attributes
os.system('cls')

class Person_2:
    current_year = 2023

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_year_birth(self):
        return Person_2.current_year - self.age
    
p3 = Person_2('João', 36)
p4 = Person_2('Lucas', 12)

print(p3.get_year_birth())
print(p4.get_year_birth())

# __dict__ and vars for instance attributes
os.system('cls')

data_joao = {'name': 'João', 'age': 36}
p5 = Person_2(**data_joao)
print(vars(p5))
print(p5.__dict__)
print(p5.__dict__['name'])


