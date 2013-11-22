#~encoding:UTF-8
import os
import time
import random

d1, d2, d3, d4, d5, d6 = '⚀', '⚁', '⚂', '⚃', '⚄', '⚅'
dice = [d1, d2, d3, d4, d5, d6]

def gen_screen(n=6):
    d = (['']*(7-n))+[random.choice(dice) for x in range(n)]
    random.shuffle(d)

    SCREEN = '''
Rolling...

   {} {}
  {} {} {}
   {} {}
'''.format(*d)
    return SCREEN


def clear():
    x = os.system('clear')

def make_random_screen():
    '''
        returns tuple of (screen,num)
    '''
    s = [' {} ']
    l = 3
    num1, num2 = (random.randrange(1,4) for x in range(2))
    top = list(s*num1)+list(' '*(l-num1))
    random.shuffle(top)
    bot = list(s*num2)+list(' '*(l-num2))
    random.shuffle(bot)
    screen = ''.join(map(str,top)) + '\n' + ''.join(map(str,bot)) + '\n'
    return (screen,num1+num2)

def get_dice(num):
    return [random.choice(dice) for x in range(num)]

def roll_dice(n=6):
    for i in range(5):
        clear()
        print gen_screen(n)
        #s, dn = make_random_screen()
        #try:
        #    print s.format(*get_dice(dn))
        #except:
        #    print s
        time.sleep(.25)

if __name__ == "__main__":
    roll_dice()

