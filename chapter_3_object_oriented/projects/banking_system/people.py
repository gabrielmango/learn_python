import account

class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age):
        self._age = age

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.name!r}, {self.age!r})'
        return f'{class_name}{attrs}'
    

class Client(Person):
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)
        self.account: account.Account | None = None

if __name__ == '__main__':
    c1 = Client('Gabriel', 28)
    c1.account = account.CurrentAccount(111, 222, 0, 0)
    print(c1)
    print(c1.account)