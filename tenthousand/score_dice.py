'''
    score_dice.py
'''

def score_dice(heldRolls):
    total = 0
    subTotal = 0
    for roll in heldRolls:
        subTotal = get_score(roll)
        total += subTotal
    return total

def get_score(roll):
    if roll[0] != 1:
        base = 100
    else:
        base = 1000
    if len(roll) == 6:
        # could be strait, doubles or 6 of a kind
        if roll.count(roll[0]) == 6:
            # six of a kind
            return ((((roll[0]*base)*2)*2)*2)
            
        else:
            # 1000 points
            return 1000
    elif len(roll) == 5:
        # five of a kind
        return (((roll[0]*base)*2)*2)
    elif len(roll) == 4:
        # four of a kind
        return ((roll[0]*base)*2)
    elif len(roll) == 3:
        # three of a kind
        return (roll[0]*base)
    else:
        # 1 or 5
        if roll[0] == 1:
            return len(roll)*100
        else:
            # fives
            return len(roll)*50

def main():
    held = ((1,),(3,3,3),(1,2,3,4,5,6),(5,),(1,1))
    print score_dice(held)
    held = ((5,5,5),(4,4,4,4),(1,),(5,),(1,1,1))
    print score_dice(held)

if __name__ == "__main__":
    main()
