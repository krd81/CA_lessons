weekly-wages
computer-cost
living-expenses
num-weeks


print("What are your weekly wages?")
weekly-wages = input()

print("What are your living expenses?")
living-expenses = input()

remainder = weekly-wages - living-expenses

print("How much does the computer cost?")
computer-cost = input()

num-weeks = computer-cost / remainder

print("It will take " + str(num-weeks) + " weeks to save the money for the computer.")


