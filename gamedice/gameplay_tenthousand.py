'''
    gamedice.gameplay_tenthousand.py
'''
from player import Player
from state import State
from choose_dice import get_choice
from dice import Roll
from die_utils import split_nums, get_tuple_from_count_dict

    WON = False
    p = Player()
    roll = Roll()
    import time
    tmp = None
    held = [][:]
    holdCount = 0
    while True:
        r = roll.get_new_roll()
        print 'Computer rolled\n{}'.format(r)
        time.sleep(1.5)
        tmp = p.ask_to_hold(r)
        if tmp:
            xtra = []
            ones, fives, others = split_nums(tmp)
            others = get_tuple_from_count_dict(others)
            for x in [ones,fives,others]:
                if len(x) >= 1 and bool(x[0]) == True:
                    xtra.append(x)
            print 'He held\n{}'.format(tmp)
            time.sleep(1.5)
            roll.hold_dice(tmp)
            holdCount += len(tmp)
            if holdCount > 15:
                print 'computer stayed'
                time.sleep(1.5)
                #if raw_input(STAY_SCREEN.format(roll.view_holds())).lower().startswith('y'):
                WON = True
                break
        else:
            if len(r) == 2:
                if r[0] == r[1]:
                    continue
            break
    if WON: 
        holds = []
        for itm in roll.get_holds():
            if len(itm) == 6:
                holds.append(itm)
                continue
            o,f,t = split_nums(itm)
            if len(t.values()) >= 1:
                t = get_tuple_from_count_dict(t)
            for x in [o,f,t]:
                if len(x) >= 1 and bool(x[0]) == True:
                    if len(x) == 1 and type(x[0]) != type(1):
                        x = x[0]
                    holds.append(x)
                    score = score_dice(holds)
        print 'He held:\n{}\nWorth {} points'.format(' '.join(map(str,holds)),score)

    else:
        holds = []
        for itm in roll.get_holds():
            if len(itm) == 6:
                holds.append(itm)
                continue
            o,f,t = split_nums(itm)
            if len(t.values()) >= 1:
                t = get_tuple_from_count_dict(t)
            for x in [o,f,t]:
                #print x
                if len(x) >= 1 and bool(x[0]) == True:
                    #print x
                    if len(x) == 1 and type(x[0]) != type(1):
                        x = x[0]
                    holds.append(x)
        score = 0
        #print get_score(itm)
        score = score_dice(holds)
        print 'He lost:\n{}\nWorth {} points'.format(' '.join(map(str,holds)),score)

    time.sleep(1.5)
