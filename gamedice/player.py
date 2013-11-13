''' 
    dice.player.py
'''
from die_utils import split_nums, get_tuple_from_count_dict
from scores import get_score, score_dice
from choose_dice import get_choice
from dice import Roll

class Player(object):
    _count = 0
    def __init__(self, name=None):
        Player._count += 1
        self._count = Player._count
        if name is None:
            self._name = 'Player#{}'.format(self._count)
            self._isHuman = False
        else:
            self._name = name
            self._isHuman = True
        self._score = 0 
        self._wins = 0

    def __str__(self):
        return self._name

    def __repr__(self):
        return str(self)

    def update_score(self,score):
        if score <= 0:
            raise ValueError
        self._score += score

    def ask_to_hold(self, dice):
        if self._isHuman:
            choice = raw_input(HOLD_SCREEN.format(dice))
        else:
            tmp = str(get_choice(dice))
            choice = ' '
            for i in tmp:
                try:
                    int(i)
                    choice += str(i) + ' '
                except:
                    pass
        return tuple(map(int,choice.split()))

HOLD_SCREEN = '''
Please choose which dice from your roll to hold.
To choose, type each die to keep and a space,
when your finished press return.

Roll --> | {} |

>> '''

STAY_SCREEN = '''

Would you like to stay with
held  --->    {}
or take your chances and keep rolling?
(Yes stay / No keep rolling) 
(y or n) >> '''


def test():
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

if __name__ == "__main__":
    test()
