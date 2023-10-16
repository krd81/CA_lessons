class Account:
    def __init__(self, account_name, initial_balance):
        self.name = account_name
        self.balance = initial_balance

    def get_balance(self):
        print(f"The account balance is: ${self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"${amount} deposited. New account balance is: ${self.balance}")


    def withdraw(self, amount):
        if (self.balance >= amount):
            self.balance -= amount
            print(f"${amount} withdrawn. New account balance is: ${self.balance}")    
        else:
            raise Exception("Insufficient funds - withdrawal not processed")
    
    def transfer(self, amount, to_acc):
        if (self.balance >= amount):
            self.balance -= amount
            to_acc.deposit(amount)
            print(f"${amount} transferrred. New account balance is: ${self.balance}")    
        else:
            raise Exception()

'''
ORIGINAL withdraw() and transfer() methods before try/except added
    def withdraw(self, amount):
        if (self.balance >= amount):
            self.balance -= amount
            print(f"${amount} withdrawn. New account balance is: ${self.balance}")    
        else:
            print(f"Insufficient funds - withdrawal not processed")
    
    def transfer(self, amount, to_acc):
        if (self.balance >= amount):
            self.balance -= amount
            to_acc.deposit(amount)
            print(f"${amount} transferrred. New account balance is: ${self.balance}")    
        else:
            print(f"Insufficient funds - transfer not processed")
'''