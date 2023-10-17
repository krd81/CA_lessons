import account, customer, address


acc1 = account.Account(customer.Customer('John Smith','20/05/1962'), 1000)
# acc1.set_address(['Unit 5C', '75 High Street','', 'Sydney', 'NSW', '2000'])


acc2 =  account.Account(customer.Customer('Mary Jones','19/09/1984'), 500)
# acc1.set_address(['Unit 1307', '308 George Street','', 'Waterloo', 'NSW', '2017'])

acc1.get_balance()
acc2.get_balance()
acc1.deposit(100)
acc2.deposit(200)
acc1.deposit(50)


# Transfer goes through
# try:
#     acc1.transfer(100, acc2)
# except:
#     print(f"Insufficient funds - transfer not processed")

# # Withdraw fails as acc2 only has $600
# try:
#     acc2.withdraw(800)
# except:
#     print(f"Insufficient funds - withdrawal not processed")

# # Teansfer fails as acc2 only has $600
# try:
#     acc2.transfer(800, acc1)
# except:
#     print(f"Insufficient funds - transfer not processed")


acc1.get_balance()
acc2.get_balance()
print(acc1.account_holder.get_customer_info())
# print(customer.get_customer_info(acc1.account_holder).__dir__)

# Link to Matt's solution
#  https://edstem.org/au/courses/13831/workspaces/