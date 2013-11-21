'''
    gameplay.py
'''
from gamedice.score import score_dice
from gamedice.dice import Roll
from gamedice.player import Player
from gamedice.state import State
from gamedice.choose_dice import get_choice

'''
    for a turn:
        while True:
            roll = Roll()
            dice = roll.get_new_roll()
            choice = get_choice(dice)
            if not choice:
                TURN_OVER
                change_player()
            else:
                tmpScore = score_dice(choice)
                if score < 1000:
                    roll_again
                else:
                    if not keep_score():
                        roll_again
                    else:
                        update_score()
                        change_player()

'''

def do_roll(player):
    roll = Roll()
    tmpScore = 0
    while True:
       if player.get_score() > 1000:
           player.onTheBoard = True
        else:
            player.onTheBoard = False
        dice = roll.get_new_roll()
        autoChoice = get_choice(dice)
        if not autoChoice:
            return tmpScore
        else:
            if not player.onTheBoard:
                print 'roll again, not at 1000'
                continue
            else:
                +





        






