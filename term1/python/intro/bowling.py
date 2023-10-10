# ```py
''' Function to calculate the frame score
    If either the first score is 10, or the sum of the first 2 scores is 10,
    then the total score is the sum of the first 3 balls
    Otherwise the score is the sum of the first 2 balls
'''
def calc_frame (ball_1, ball_2, ball_3):
    if ball_1 == 10 or ball_1 + ball_2 == 10:
        score = ball_1 + ball_2 + ball_3
    else:
        score = ball_1 + ball_2
    return score


''' Additional code added to check for incorrect input
    Negative numbers or a score >10 will cause function to return false
'''
def check_input(ball_score):    
    if(ball_score < 0 or ball_score > 10):
        # int(input("Incorrect input - please try again"))
        return False
    else:
        return True
        


# main

#  Ask user for first score
ball_1 = int(input("1st ball score: "))
''' if number entered is incorrect - ask user to re-enter
    Keeps asking user to re-enter as long as the input is invalid
    Once valid, the loop ends
'''
while check_input(ball_1) == False:
    print("Incorrect input - please try again")
    ball_1 = int(input("1st ball score: "))
    check_input(ball_1)

# Repeat for 2nd & 3rd scores
ball_2 = int(input("2nd ball score: "))

while check_input(ball_2) == False:
    print("Incorrect input - please try again")
    ball_2 = int(input("2nd ball score: "))
    check_input(ball_2)


ball_3 = int(input("3rd ball score: "))

while check_input(ball_3) == False:
    print("Incorrect input - please try again")
    ball_3 = int(input("3rd ball score: "))
    check_input(ball_3)


# When 3 valid scores have been entered, the frame score is calculated
# by calling the calc_frame function
frame_score = calc_frame(ball_1, ball_2, ball_3)

print(f"The frame score is: {frame_score}" )

# ```