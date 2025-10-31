# Score categories.
# Change the values as you see fit.
YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11


def score(dice, category):
    if category in range(1,7):
        return numbers(dice,category)

    if category==FULL_HOUSE:
        unicos=set(dice)
        if len(unicos)==2:
            if dice.count(list(unicos)[0]) in [2,3]:
                return sum(dice)

    if category==FOUR_OF_A_KIND:
        unicos=set(dice)
        if len(unicos)<=2:
            for num in list(unicos):
                if dice.count(num)>=4:
                    return num*4
                    
    if category==LITTLE_STRAIGHT:
        if set([1,2,3,4,5])-set(dice)==set():
            return 30
            
    if category==BIG_STRAIGHT:
        if set([2,3,4,5,6])-set(dice)==set():
            return 30

    if category==CHOICE:
        return sum(dice)

    if category==YACHT:
        unicos=set(dice)
        if len(unicos)==1:
            return 50
    return 0

def numbers(dice, value):
    return dice.count(value)*value
