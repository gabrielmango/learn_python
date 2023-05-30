# THEORY: Inheritance, generalization and specialization
import os
os.system('cls')

class Person:
    age = 28
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name

    def say_name_class(self):
        print(self.name, self.last_name)
        print(self.__class__.__name__)

class Client(Person):
    pass

class Student(Person):
    pass

c1 = Client('Gabriel', 'Mango')
c1.say_name_class()
print(c1.age)

s1 = Student('Mateus', 'Lucas')
s1.say_name_class()
s1.age = 25
print(s1.age)

# Super and Overriding Members in Object Oriented Python
os.system('cls')

class A:
    attribute_a = 'value A'

    def __init__(self, attribute):
        self.attribute = attribute

    def method(self):
        print('A')

class B(A):
    attribute_b = 'value B'

    def __init__(self, attribute, another_attribute):
        super().__init__(attribute)
        self.another_attribute = another_attribute

    def method(self):
        print('B')

class C(B):
    attribute_c = 'value C'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def method(self):
        super(B, self).method()
        super().method()
        print('C')

c = C('attribute', 'another attribute')
c.method()

print(c.attribute_a)
print(c.attribute_b)
print(c.attribute_c)

print(c.attribute)
print(c.another_attribute)
