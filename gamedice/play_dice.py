'''
    play_dice.py
'''
from scores import score_dice
from player import Player
from dice import Roll
from die_utils import process_single_hold
from process_score import Scorer
from state import State
import os

def clear():
    x = os.system('clear')
    

p1, p2 = Player('kyle'),Player('joe')
dice = Roll()
scorer = Scorer()
tmpScore = 0
while True:
    clear()
    current = p1.get_current()
    print 'Rolling: {} Score: {}'.format(current.get_name(),current.get_score())
    roll = dice.get_new_roll()
    print 'rolled: {}'.format(roll)
    raw_input()
    clear()
    held = current.ask_to_hold(roll)
    heldp = process_single_hold(held)
    print 'Held: {}'.format(' '.join(map(str,heldp)))
    print score_dice(heldp)
    print score_dice(held)
    print held
    if list(held) == [(),()]:

        current = current.change_player()
        tmpScore = 0
        dice = Roll()
        continue
    else:
        dice.hold_dice(held)
        tmpScore += score_dice(held)
        print 'Temp Score: {}'.format(tmpScore)
        raw_input()
        if current.get_score() >= 1000 or score_dice(held) >= 1000:
            if current.ask_to_continue():
                continue
            else:
                current.update_score(tmpScore)
                tmpScore = 0 
                current.change_player()
                continue
        else:
            continue
