credit_card_number = str(input())

if (credit_card_number[0]) == '4':
    if ((credit_card_number.len() == 13 or credit_card_number.len() == 16)):
        print("Valid Visa card number")
        print("The bank number is: " + credit_card_number[1:6])
        print("The account number is: " + credit_card_number[6:-1])        
    else:
        print("Invalid Visa card number")
else:
    print("Not a Visa card")