class Customer:
    def __init__(self, first_name, last_name, address, dob):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.dob = dob

    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class BankAccount:
    def __init__(self, customer, initial_balance):
        self.customer = customer
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount
        return amount

    def withdraw(self, amount):
        # Assume they can't empty the account
        if amount < self.balance:
            self.balance -= amount
            return amount
        else:
            return 0

    def transfer(self, amount, to_account):
        return to_account.deposit(self.withdraw(amount))



# Main
acc1 = BankAccount(Customer('John', 'Smith', '12 Any Street, Brisbane QLD 4000', '10/10/1980'), 1000)
acc2 = BankAccount(Customer('Mary', 'Jones', '25 High Street, Brisbane QLD 4000', '05/11/1992'), 500)

# print(acc1.balance)    # 1000
# acc1.deposit(100)
# acc2.deposit(200)
# acc1.deposit(50)
# print(acc2.balance)    # 700
# print(acc1.balance)    # 1150
# print(acc1.withdraw(2000)) # 0
# print(acc1.balance)        # 1150
# print(acc1.withdraw(500))  # 500
# print(acc1.balance)        # 650
# print(acc1.transfer(2000, acc2)) # 0
# print(acc1.balance)        # 1150
print(acc1.transfer(500, acc2)) # 500
# print(acc1.balance) # 650
# print(acc2.balance) # 1200
# print(acc1.customer.full_name())









