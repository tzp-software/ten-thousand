# coding: utf-8
from dice import Roll
from choose_dice import get_choice
from scores import score_dice
from state import State
from die_utils import clear

class DiceState(State):
    def __init__(self,info):
        super(State,self).__init__()
        self.score = 0
    

def start_roll():
    players = [State(1),State(2),State(3)]
    while True:
        current = State.get_current()
        roll = Roll()
        tmpScore = 0
        while True:
            clear()
            print 'its player {}\'s turn'.format(current.id)
            d = roll.get_new_roll()
            print 'Rolled:\n{}'.format(d)
            c = get_choice(d)
            if not c:
                print 'damn i lost my turn',
                if tmpScore > 0:
                    print 'and i lost {} points, lame'.format(tmpScore)
                break
            raw_input('thinking about what i want to hold....')
            roll.hold_dice(c)
            print 'I held:\n{}\nThats worth {} points'.format(c,score_dice(c))
            tmpScore += score_dice(c)
            if tmpScore != score_dice(c): 
                print '{} points so far this roll'.format(tmpScore)
            if raw_input('press enter to keep rolling\nor q to quit now and keep {} points '.format(tmpScore)).lower() == 'q':
                current.set_score(tmpScore)
                current.change_state()
            clear()
        print 'press enter to go again, or q to quit',
        quit = raw_input()
        if quit == 'q':
            break
        else:
            current.change_state()
            tmpScore = 0
            clear()
            continue
        #current.score +=  tmpScore
        
print start_roll()