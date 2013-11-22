'''
    ai_action.py
'''
import time
from dice import Roll
from roll_screen import roll_dice, clear
from scores import score_dice
from choose_dice import  get_choice

'''
    api:
        roll = Roll()
        dice = roll.get_new_roll()
        print 'Rolled: {}'.format(dice)
        choice = get_choice(dice)
        print 'Holding: {}'.format(choice)
        print 'Worth: {}'.format(score_dice(choice))
'''
def ai():
    while True:
        roll = Roll()
        tmp = 0
        while True:
            dice = roll.get_new_roll()
            roll_dice(len(roll))
            clear()
            print 'Rolled: {}'.format(' '.join(map(str,dice)))
            raw_input()
            choice = get_choice(dice)
            print 'thinking',
            for i in range(4):
                t = '.'*i
                print t,
                time.sleep(.5)
            raw_input()
            if len(choice) == 0:
                if len(dice) == 2 and dice[0] == dice[1]:
                    print 'Doubles Roll again'
                    raw_input()
                    continue
                print 'Turn over!\nPress q to quit or just enter to play again',
                c = raw_input()
                if c == 'q':
                    import sys
                    sys.exit()
                else:
                    break
            else:
                print 'Holding: {}'.format(choice)
                roll.hold_dice(choice)
                s = score_dice(choice)
                print 'Worth: {} points'.format(s)
                tmp += int(s)
                if tmp != s:
                    print 'Now youve got {} points.'.format(tmp)
                raw_input()
                if tmp >= 1000:
                    print 'Would you like to stop and keep {} points?\n(y or n):'.format(tmp),
                    if raw_input().lower().startswith('y'):
                        print 'Kept: {}'.format(tmp)
                        tmp = 0
                        raw_input()
                        break
                continue
        


if __name__ == "__main__":
    ai()
