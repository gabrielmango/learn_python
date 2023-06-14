import account
import people

class Bank:
    def __init__(
        self,
        agencies: list[int] | None = None,
        clients: list[people.Person] | None = None,
        accounts: list[account.Account] | None = None,                 
    ):
        self.agencies = agencies or []
        self.clients = clients or []
        self.accounts = accounts or []

    def is_agency(self, agency: account.Account):
        if agency.account in self.agencies:
            return True
        return False
    
    def is_client(self, client):
        if client in self.clients:
            return True
        return False
    
    def is_account(self, account):
        if account in self.accounts:
            return True
        return False
    
    def is_client_account(self, client: people.Person, account):
        if account in client.account:
            return True
        return False
    
    def authenticate(self, client: people.Person, account: account.Account):
        return self.is_agency(account) and \
            self.is_client(client) and \
            self.is_account(account) and \
            self.is_client_account(client, account)
    
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencies!r}, {self.accounts!r}, {self.clients!r})'
        return f'{class_name}{attrs}'
