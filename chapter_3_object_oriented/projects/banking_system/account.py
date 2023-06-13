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
        print('---')

class SavingsAccount(Account):
    def withdraw_money(self, value):
        value_after_withdrawal = self.balance - value

        if value_after_withdrawal >= 0:
            self.balance -= value
            self.details(f'(WITHDRAW) {value}')
            return self.balance
        
        print('Unable to withdraw desired amount!')
        self.details(f'(WITHDRAW DENIED) {value}')    


if __name__ == '__main__':
    savings_account_1 = SavingsAccount(111, 222, 0)
    savings_account_1.withdraw_money(1)
    savings_account_1.cash_deposit(1)
    savings_account_1.withdraw_money(1)