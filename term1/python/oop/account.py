import customer

class Account:
    def __init__(self, account_holder, initial_balance):
        self.account_holder = customer.Customer('name', 'DOB')
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

