'''
    gamedice.choose_dice.py
'''
from scores import get_counts

def get_choice(roll):
    rtn = []
    diceLeft = len(roll)
    if len(roll) == 6:
        # check 6 of a kind, strait or doubles
        # this is doubles
        if get_counts(roll).values().count(2) == 3:
            # just return the roll
            rtn.append(tuple(roll))
            # and kill the count
            diceLeft -= 6
        # this is s a strait
        if get_counts(roll).values().count(1) == 6:
            # just return the roll
            rtn.append(tuple(roll))
            # and kill the count
            diceLeft -= 6
        # this is six of a kind
        if get_counts(roll).values().count(6) == 1: 
            # just return the roll
            rtn.append(tuple(roll))
            # and kill the count
            diceLeft -= 6
    
    if len(roll) >= 5:
        if get_counts(roll).values().count(5) == 1: # 5 of a kind
            tmp = []
            if diceLeft >= 5:
                for d in range(len(roll)):
                    if diceLeft > 0:
                        if roll.count(roll[d]) == 5:
                            tmp.append(roll[d])
                            diceLeft -= 1
            if len(tmp) >=1:
                rtn.append(tuple(tmp))
            tmp = []

    if len(roll) >= 4:
        if get_counts(roll).values().count(4) == 1: # 4 of a kind
            tmp = []
            if diceLeft >= 4:
                for d in range(len(roll)):
                    if diceLeft > 0:
                        if roll.count(roll[d]) == 4:
                            tmp.append(roll[d])
                            diceLeft -= 1
            if len(tmp) >= 1:
                rtn.append(tuple(tmp))
            tmp = []

    if len(roll) >= 3:
        if 2 >= get_counts(roll).values().count(3) >= 1: # one or two 3 of a kind
            tmp = []
            if diceLeft >= 3:
                for d in range(len(roll)):
                    if diceLeft > 0:
                        if roll.count(roll[d]) == 3:
                            tmp.append(roll[d])
                            diceLeft -= 1
            if len(tmp) >= 1:
                if len(tmp) == 6:
                    tmp.sort()
                    tmp = (tuple(tmp[:3]),tuple(tmp[3:]))
                rtn.append(tuple(tmp))
            tmp = []
    if diceLeft > 0:
        if 1 in roll:
            if get_counts(roll)['1'] <= 2:
                tmp = []
                for d in roll:
                    if d == 1:
                        tmp.append(d)
                if len(tmp) >=1:
                    rtn.append(tuple(tmp))
                tmp = []
        if 5 in roll:
            if get_counts(roll)['5'] <= 2:
                tmp = []
                for d in roll:
                    if d == 5:
                        tmp.append(d)
                if len(tmp) >= 1:
                    rtn.append(tuple(tmp))
    return rtn


def main():
    from dice import Roll
    roll = Roll()
    d = roll.get_new_roll()
    print 'Rolled:\n{}'.format(d)
    print 'Held:\n{}'.format(get_choice(d))

if __name__ == "__main__":
    main()
    
