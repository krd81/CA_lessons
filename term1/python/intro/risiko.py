import random

attacker_roll = []
defender_roll = []
num_dice_attacker = 3
num_dice_defender = 3

# roll function is responsible for 'rolling' the die and adding the
# random numbers generated to the arrays
def roll (num_dice_attacker, num_dice_defender):
    for i in range(num_dice_attacker):
        die_roll = random.randint(1,6)
        attacker_roll.append(die_roll)

    for i in range(num_dice_defender):
        
        die_roll = random.randint(1,6)
        defender_roll.append(die_roll)

    print(f'{attacker_roll} , {defender_roll}')
    return [attacker_roll, defender_roll]


def battle (rolls, num_dice_attacker, num_dice_defender):

    attacker_roll = rolls[0]
    defender_roll = rolls[1]
    min_dice = min(len(attacker_roll), len(defender_roll))
    attacker_roll.sort(reverse = True)
    defender_roll.sort(reverse = True)

    for i in range(min_dice):
        count = 0
        if(attacker_roll[i] > defender_roll[i]):
            # count is no. attack wins (or defender loses)
            count += 1
    

    num_dice_defender -= count    
    num_dice_attacker -= (min_dice-count)
    
    print(f'DEF losses: {count}')
    print('\n')
    # Returns the number of defender loses and the number of dice each side has remaining
    return count, num_dice_attacker, num_dice_defender


# START GAME
# ROLL DICE (EACH TEAM STARTS WITH 3 DICE EACH)
# BATTLE : THE SCORES ARE COMPARED AND THE NUMBER OF DICE ARE UPDATED
# PROCESS KEEPS GOING UNTIL 1 SIDE HAS 0 DICE

# while (num_dice_attacker > 0 and num_dice_defender > 0):
roll (num_dice_attacker, num_dice_defender)

# battle (roll(num_dice_attacker, num_dice_defender),num_dice_attacker, num_dice_defender)



'''
game([3, 6, 4],[5, 5, 2])
1. ATT(6) VS DEF(5): DEF LOSES

GAME([3, 6, 4],[5, 2])
2. ATT(4) VS DEF(5): ATT LOSES
3. ATT(3) VS DEF(2): DEF LOSES
ATTACK HAS 2 ARMIES
DEFENCE HAS 1 ARMY

POSSIBLE OUTCOMES: DEFENCE LOSES 0, 1, 2, 3 ARMIES
IF DEF LOSE 3 ARMIES, ATTACK HAS WON
IF DEF LOSE 2 ARMIES: THEN NEXT ROUND ATTACK HAS 2, DEFENCE HAS 1
    POSSIBLE OUTCOMES: DEFENCE LOSES 0, 1 ARMY
    IF DEF LOSE 1 ARMY, ATTACK HAS WON
    IF DEF LOSE 0 ARMIES: THEN NEXT ROUND ATTACK HAS 1, DEFENCE HAS 1
        WHOEVER WINS THE NEXT ROUND IS THE OVERALL WINNER
IF DEF LOSE 1 ARMY: THEN NEXT ROUND ATTACK HAS 1, DEFENCE HAS 2
    IF DEF LOSE 0 ARMIES, DEFENCE HAS WON
    IF DEF LOSE 2 ARMIES, ATTACK HAS WON
    IF DEF LOSE 1 ARMY: THEN NEXT ROUND ATTACK HAS 1, DEFENCE HAS 1
        WHOEVER WINS THE NEXT ROUND IS THE OVERALL WINNER
IF DEF LOSE 0 ARMIES, DEFENCE HAS WON
'''