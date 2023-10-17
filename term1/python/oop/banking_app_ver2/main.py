'''
VERSION 2 created to practise COMPOSITION using banking example
'''


class Account:
    def __init__(self, customer, initial_balance):
        self.customer = customer
        self.balance = initial_balance

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return amount

    def withdraw(self, amount):
        if  self.balance >= amount:
            self.balance -= amount
        else:
            amount = 0
        return amount

    def transfer(self, amount, to_acc):
        return to_acc.deposit(self.withdraw(amount))


class Customer:
    def __init__(self, first_name, last_name, address, dob):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.dob = dob

class Address:
    def __init__(self, address_1, address_2, suburb, state, post_code):
        self.address_1 = address_1
        self.address_2 = address_2
        self.suburb = suburb
        self.state = state
        self.post_code = post_code

    def get_address(self):
        self.address = [self.address_1, self.address_2, self.suburb, self.state, self.post_code]
        return self.address

# Main

# acc1 = Account('John Smith', 1000)
# acc2 = Account('Mary Jones', 500)


acc1 = Account(Customer('John', 'Smith', Address('Unit 3', '490 Main Road', 'Manly', 'NSW', '2095'), '20/04/1988'), 1000)
acc2 = Account(Customer('Mary', 'Jones', Address('Level 4', '37 Addison Lane', 'Banksmeadow', 'NSW', '2135'), '30/09/1975'), 500)


## BASIC LEVEL TESTS:
print(acc1.get_balance())    # 1000
acc1.deposit(100)
acc2.deposit(200)
acc1.deposit(50)
print(acc2.get_balance())    # 700
print(acc1.get_balance())    # 1150

## EXTENDED LEVEL TESTS
# print(acc1.withdraw(100))  # 100
# print(acc2.withdraw(800))  # 0
# print(acc1.transfer(250, acc2)) # 250
# print(acc1.get_balance())   # 750
# print(acc2.get_balance())   # 750

# print(acc2.transfer(1000, acc1)) # 0
# print(acc2.transfer(100, acc1)) # 100

# print(acc1.get_balance())   # 850
# print(acc2.get_balance())   # 650


# ADVANCED LEVEL TESTS
print(f"{acc1.customer.first_name} {acc1.customer.last_name}, account balance: ${acc1.get_balance()}")
print(f"{acc2.customer.first_name} {acc2.customer.last_name}, address: {acc2.customer.address.get_address()}")
print(f"{acc1.customer.first_name} {acc1.customer.last_name}, Suburb: {acc1.customer.address.suburb}, State: {acc1.customer.address.state}")
print(f"{acc2.customer.first_name} {acc2.customer.last_name}, Suburb: {acc2.customer.address.suburb}, State: {acc2.customer.address.state}")