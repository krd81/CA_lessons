import account

acc1 =  account.Account('John Smith', 1000)
acc2 =  account.Account('Mary Jones', 500)

# acc1.get_balance()
# acc2.get_balance()
# acc1.deposit(100)
# acc2.deposit(200)
# acc1.deposit(50)

# acc2.withdraw(800)

# Transfer goes through
try:
    acc1.transfer(100, acc2)
except:
    print(f"Insufficient funds - transfer not processed")

# Withdraw fails as acc2 only has $600
try:
    acc2.withdraw(800)
except:
    print(f"Insufficient funds - withdrawal not processed")

# Teansfer fails as acc2 only has $600
try:
    acc2.transfer(800, acc1)
except:
    print(f"Insufficient funds - transfer not processed")


acc1.get_balance()
acc2.get_balance()