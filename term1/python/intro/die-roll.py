import random

dice_rolls = []

nds = input("What is the game format (nds): ")

def roll (nds):
    if (nds[0].isnumeric and nds[-1].isnumeric and nds.find('d')>0):
        d_pos = nds.find('d')    # Needed as an anchor point to be able to get the positions of the 1st & 2nd number

        num_rolls = int(nds[:d_pos])
        num_sides = int(nds[d_pos+1:])
    else:
        return None

        return num_rolls, num_sides

def game_play(num_rolls, num_sides):
    for i in range(num_rolls):
        roll = random.randint(1,num_sides)
        
        dice_rolls.append(roll)
    print(dice_rolls)
    
    sum_rolls = 0
    max_roll = 0

    for i in range(num_rolls):
        sum_rolls += dice_rolls[i]
        if (dice_rolls[i] > max_roll):
            max_roll = dice_rolls[i]
    print(f"The sum of the dice rolls is {sum_rolls}")
    print(f"The max value of the dice rolls is {max_roll}")


# Couldn't get the format checking to working inside the function, so added
# if statement before calling the game_play
if (nds[0].isnumeric and nds[-1].isnumeric and nds.find('d')>0):
    game_play(roll(nds)[0] , roll(nds)[1])
else:
    print("Incorrect input")
