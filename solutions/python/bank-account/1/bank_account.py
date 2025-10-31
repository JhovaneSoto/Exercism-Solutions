class BankAccount:
    def __init__(self):
        self.balance=0
        self.status_open=False

    def get_balance(self):
        if not self.status_open:
            raise ValueError("account not open")
        return self.balance

    def open(self):
        if self.status_open:
            raise ValueError("account already open")
        self.balance=0
        self.status_open=True

    def deposit(self, amount):
        if amount<=0:
            raise ValueError('amount must be greater than 0')
        if not self.status_open:
            raise ValueError("account not open")
        self.balance+=amount

    def withdraw(self, amount):
        if amount<=0:
            raise ValueError('amount must be greater than 0')
        if not self.status_open:
            raise ValueError("account not open")
            
        if self.balance>=amount:
            self.balance-=amount
        else:
            raise ValueError('amount must be less than balance')

    def close(self):
        if not self.status_open:
            raise ValueError("account not open")
        self.status_open=False
