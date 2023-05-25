import os
os.system('cls')

class Car:
    def __init__(self, name):
        self.name = name
        self._motor = None
        self._factory = None
    
    def car_information(self):
        return f'Name: {self.name}, Factory: {self._factory.name}, Motor: {self._motor.name}'
    
    @property
    def motor(self):
        return self._motor
    @motor.setter
    def motor(self, value):
        self._motor = value

    @property
    def factory(self):
        return self._factory
    @factory.setter
    def factory(self, value):
        self._factory = value

class Motor:
    def __init__(self, name):
        self.name = name

class Factory:
    def __init__(self, name):
        self.name = name

motor_1_0 = Motor('1.0')
motor_2_0 = Motor('2.0')

fiat = Factory('Fiat')

argo_1 = Car('Argo verson 1')
argo_1.motor = motor_1_0
argo_1.factory = fiat
print(argo_1.car_information())

argo_2 = Car('Argo verson 2')
argo_2.motor = motor_2_0
argo_2.factory = fiat
print(argo_2.car_information())