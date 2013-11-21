'''
    gamedice.scores.py
'''

COUNT_MAP = {
    '1':0,'2':0,
    '3':0,'4':0,
    '5':0,'6':0
            }

def get_counts(roll):
    rtn = COUNT_MAP.copy()
    for d in roll:
        rtn[str(d)] += 1
    return rtn

def is_strait(dice):
    return get_counts(dice).values().count(1) == 6

def is_doubles(dice):
    return get_counts(dice).values().count(2) == 3
 
def score_dice(heldRolls):
    total = 0
    subTotal = 0
    for roll in heldRolls:
        subTotal = get_score(roll)
        total += subTotal
    return total

def get_score(roll):
    '''
        this function can only take dice already 
        seperated by number ie: (1,1,1) or (5,5) not (1,1,5) 
        thats what die_utils:split_nums(nums) is for
    '''
    if len(roll) == 0:
        return 0
    if roll[0] != 1:
        base = 100
    else:
        base = 1000
    if len(roll) == 6:
        # could be strait, doubles or 6 of a kind
        if roll.count(roll[0]) == 6:
            # six of a kind
            return (((int(roll[0])*base)*2)*2)*2
        else: # its either doubles or a strait
            # 1000 points
            return 1000
    elif len(roll) == 5:
        # five of a kind
        return ((int(roll[0])*base)*2)*2
    elif len(roll) == 4:
        # four of a kind
        return (int(roll[0])*base)*2
    elif len(roll) == 3:
        # three of a kind
        try:
            return int(roll[0])*base
        except:
            try:
                return int(roll[0][0])*base
            except:
                return 0
    else:
        # 1 or 5
        if roll[0] == 1:
            return len(roll)*100
        else:
            # fives
            return len(roll)*50


#def test():
#    roll = Roll()
#    d = roll.get_new_roll()
#    print 'The Roll:\n{}'.format(d)
#    print 'The counts:\n{}'.format(get_counts(d))


def main():
    held = ((1,),(3,3,3),(1,2,3,4,5,6),(5,),(1,1))
    print score_dice(held)
    held = ((5,5,5),(4,4,4,4),(1,),(5,),(1,1,1))
    print score_dice(held)
    
if __name__ == "__main__":
    #test()
    main()
