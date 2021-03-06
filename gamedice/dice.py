# dice.py
import random
from die_utils import split_nums, get_tuple_from_count_dict
from scores import get_score
from choose_dice import get_choice


class DieCountError(Exception):
    pass


def get_nums_from_strs(strs):
    rtn = [][:]
    for c in strs:
        try:
            rtn.append(int(c))
        except:
            pass
    return rtn


class Roll(object):
    _defaultDieNum = 6
    def __init__(self, dieNum=None):
        if dieNum is None:
            self.dieNum = Roll._defaultDieNum
        else:
            self.dieNum = dieNum
        self.currentCount = self.dieNum
        self.currentRoll = [][:]
        self.heldDice = [][:]

    def __str__(self):
        return ' '.join(map(str,self.currentRoll))

    def __repr__(self):
        return str(self.currentRoll)

    def __len__(self):
        return self.currentCount

    def get_new_roll(self):
        if self.currentCount == 0:
            self.currentCount = self.dieNum
        self.currentRoll = [random.randrange(1,7) for die in range(self.currentCount)]
        return self.currentRoll[:]

    def hold_dice(self,dice):
        d = []
        for itm in dice:
            print repr(itm)
            if not itm == ' ':
                d.append(itm)
        print d
        #dice = get_nums_from_strs(d)
        if len(d) > self.currentCount:
            raise DieCountError, d
        for x in d:
            if len(x) == 1:
                self.currentCount -= 1
            elif len(x) > 1:
                for i in x:
                    try:
                        int(i)
                        if int(i) >= 1:
                            self.currentCount -= 1
                    except:
                        pass
            else:
                pass
            if not x == ' ':
                self.heldDice.append(x)

    def view_holds(self):
        return ' '.join(map(str,self.heldDice))

    def get_holds(self):
        rtn = self.heldDice[:]
        self.heldDice = [][:]
        self.currentCount = self.dieNum
        return rtn

    def get_held_score(self):
        rtn = 0
        for itm in self.heldDice:
            nums = list(split_nums(itm))
            nums[2] = get_tuple_from_count_dict(nums[2])
            print nums[0]
            print nums[1]
            print nums[2]
            for itm in nums:
                if len(itm) >= 1:
                    print get_score(itm)
            #rtn += get_score(nums)
        return rtn



#r = Roll()
#d = r.get_new_roll()
#r.hold_dice(get_choice(d))
#d = r.get_new_roll()
#r.hold_dice(get_choice(d))
#d = r.get_new_roll()
#r.hold_dice(get_choice(d))
#r.get_held_score()
