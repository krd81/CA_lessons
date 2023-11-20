def decimal_to_binary(decimal):
    # Take your previous solution 

	result = []	
	x = decimal

	while (x > 1):
		x = decimal // 2
		if (decimal % 2 > 0):
			result.append("1")
		else:
			result.append("0")
		
		if x ==1 :
			result.append("1")
		decimal = x
	
	
	result.reverse()
	string = ''

	for x in result:
		string += x

	#print(result)
	#print(string)
	return result.reverse()

def exclusive_or(num1, num2):
    binary_1 = []
    binary_2 = []
    binary_1 = decimal_to_binary(num1)
    binary_2 = decimal_to_binary(num2)

    try:
        length = max(len(binary_1), len(binary_2))
    except TypeError:
        length = 0

    # Create new binary numbers of the correct length for comparison    
    new_binary_1 = create_new_binary(binary_1, length)
    new_binary_2 = create_new_binary(binary_2, length)
    result_binary = []

    # Perform the XOR function
    # Starting from highest element means result_binary is in correct order
    n = length-1
    while (n >= 0):
        if(new_binary_1[n] == new_binary_2[n]):
            result_binary.extend('0')
        else:
            result_binary.extend('1')
        n -= 1
    
    string = ''

    for x in result_binary:
        string += x
    
    print(f'The result is {string} in binary, which is {int(string, 2)} in decimal')

    return int(string,2)





def create_new_binary(binary_number, length):
    new_binary = []
    new_binary.extend(binary_number)
    var = length - len(binary_number)

    if (var > 0):
        n = 0
        while(n < var):
            new_binary.extend('0')
            n += 1


    return new_binary
    
exclusive_or(7, 3)