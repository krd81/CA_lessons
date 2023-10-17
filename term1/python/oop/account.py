import customer, address

class Account:
    def __init__(self, account_holder, initial_balance):
        self.account_holder = customer.Customer('name', 'DOB')
        self.balance = initial_balance
        # self.addr = []

    # def set_address(self, address):
        # self.addr = address.Address(address)



    def get_balance(self):
        print(f"The account balance is: ${self.balance}")

    def deposit(self, amount):
        self.balance += amount
        return amount


    def withdraw(self, amount):
        if (self.balance >= amount):
            self.balance -= amount              
        else:
            amount = 0
        return 0
    
    def transfer(self, amount, to_acc):
        return self.withdraw(to_acc.deposit(amount))



