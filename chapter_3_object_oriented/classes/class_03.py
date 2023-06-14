# Encapsulation (access modifiers: public, _protected, __private)
import os
from typing import Any
os.system('cls')

# no underscore = public
# _ an underscore = protected
# __ two underscores = private

class Foo:
    def __init__(self):
        self.public = 'this is public.'
        self._protected = 'this is protected'
        self.__private = 'this is private'
    
    def public_method(self):
        return 'public_method'
    
    def _protected_method(self):
        return '_protected_method'
    
    def __private_method(self):
        return '__private_method'

# Relations between classes: association, aggregation and composition

#association
os.system('cls')

class Writer:
    def __init__(self, name):
        self.name = name
        self._tool = None

    @property
    def tool(self):
        return self._tool
    @tool.setter
    def tool(self, value):
        self._tool = value

class WritingTool:
    def __init__(self, name):
        self.name = name
    def write(self):
        return f'{self.name} is writing.'

writer = Writer('Gabriel')

pen = WritingTool('blue pen')
typewriter = WritingTool('typewriter')

writer.tool = pen
print(writer.tool.write())

writer.tool = typewriter
print(writer.tool.write())

#aggregation
os.system('cls')

class ShoppingCart:
    def __init__(self):
        self._products = []

    def insert_products(self, *products):
        self._products.extend(products)
    
    def list_products(self):
        print()
        for product in self._products:
            print(product.name, product.price)
        print()

    def sum_products(self):
        return sum([p.price for p in self._products])

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

shopping_cart = ShoppingCart()
p1, p2 = Product('Pen', 1.20), Product('notebook', 20)
shopping_cart.insert_products(p1,p2)
shopping_cart.list_products()
print(shopping_cart.sum_products())

#composition
os.system('cls')

class Client:
    def __init__(self, name):
        self.name = name
        self.adresses = []
    
    def insert_address(self, street, number):
        self.adresses.append(Address(street, number))
    
    def list_address(self):
        for address in self.adresses:
            print(address.street, address.number)

class Address:
    def __init__(self, street, number):
        self.street = street
        self.number = number

client1 = Client('Gabriel')
client1.insert_address('St. Brasil', 65)
client1.insert_address('St. Ubatuba', 74)

client1.list_address()