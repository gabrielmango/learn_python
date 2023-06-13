import abc

class Account(abc.ABC):
    def __init__(self, agency, account, balance):
        self.agency = agency
        self.account = account
        self.balance = balance

    @abc.abstractmethod
    def withdraw_money(self, value): ...

    def cash_deposit(self, value):
        self.balance += value
        self.details(f'(DEPOSIT) {value}') 

    def details(self, message = ''):
        print(f'Your balance is {self.balance:.2f} {message}')