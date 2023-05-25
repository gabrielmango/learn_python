# Class methods (@classmethod) + factories methods
import os
os.system('cls')

class Person:
    year = 2023

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def class_method(cls):
        print('Hello!')
    
    @classmethod
    def create_age_fifty(cls, name):
        return cls(name, 50)
    
    @classmethod
    def create_without_name(cls, age):
        return cls('anonymous', age)
    
p1 = Person('Gabriel', 28)
print(p1.__dict__)
Person.class_method()
p2 = Person.create_age_fifty('Helena')
print(p2.__dict__)
p3 = Person.create_without_name(25)
print(p3.__dict__)

# @staticmethod (static methods) are useless in Python
os.system('cls')

class Classe:
    @staticmethod
    def function_class(*args, **kwargs):
        print(args, kwargs)

def function_without_class(*args, **kwargs):
     print(args, kwargs)

c1 = Classe()
c1.function_class()
function_without_class()

# method vs @classmethod vs @staticmethod
os.system('cls')

class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.password = password

    @classmethod
    def create_with_auth(cls, user, password, host):
        connection = cls()
        connection.user = user
        connection.password = password
        connection.host = host
        return connection
    
    @staticmethod
    def log(mgs):
        print('LOG ', mgs)

def connection_log(mgs):
    print('LOG ', mgs)

c1 = Connection.create_with_auth('gabriel', '123', 'localhost/8080')
print(c1.__dict__)
print(Connection.log('This is a mensage of log.'))

c2 = Connection()
c2.set_user('Mateus')
c2.set_password('321')
print(c2.__dict__)

# @property + @setter - getter e setter no modo Pythônico
os.system('cls')

class Pen:
    def __init__(self, color):
        self.color = color
        self.type = None
    
    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, value):
        self._color = value

    @property
    def type(self):
        return self._type
    
    @type.setter
    def type(self, value):
        self._type = value
    

pen_1 = Pen('blue')
print(pen_1.color)
print(pen_1.type)

pen_1.color = 'pink'
pen_1.type = 'plastic'

print(pen_1.color)
print(pen_1.type)