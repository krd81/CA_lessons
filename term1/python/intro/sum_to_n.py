n = int(input("What number do you want to sum to? "))


def sum_to_n(number):
    result = 0
    count = 0
    
    while (count < number+1) :
        result += count
        count += 1


    print(f"The sum of 1 to {number} is {result}")

sum_to_n(n)
