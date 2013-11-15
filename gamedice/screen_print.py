import random
import time
from pyfiglet import Figlet

SCREEN = '''




{}      





'''



def clear():
    import os
    x = os.system('clear')

def print_info(info):
    clear()
    print SCREEN.format(info)
    time.sleep(.08)

f = Figlet()
for i in range(10):
    num = [random.randrange(1,7) for x in range(6)]
    num = '   '.join(map(str,num))
    i = f.renderText(num)
    print_info(i)


