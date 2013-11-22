#encoding:UTF-8
'''
    screens.py
'''
#__all__ = [splash]
from pyfiglet import Figlet
from die_utils import process_single_hold
from dice import Roll
from roll_screen import roll_dice
from choose_dice import get_choice
from scores import score_dice
import os


def get_txt(txt):
    f = Figlet(font='small')
    return f.renderText(txt)

def clear():
    x = os.system('clear')

splash = '''
 _____       _____ _                              _
|_   _|__ _ |_   _| |_  ___ _  _ ___ __ _ _ _  __| |
  | |/ -_) ' \| | | ' \/ _ \ || (_-</ _` | ' \/ _` |
  |_|\___|_||  _| |_||_\___/\_,_/__/\__,_|_||_\__,_|
           _  __   __   __   __
          / |/  \ /  \ /  \ /  \    ⚃     ⚂     ⚀
          | | () | () | () | () |      ⚄     ⚁    ⚅
          |_|\__( )__/ \__/ \__/
                |/

            Press enter to start...

by: Kyle Roux
'''


menu = '''
 _ 
/ |    ##  #           #       ##             
| |   #   ###  ## ### ###     #    ## ### ### 
|_|o   #   #  # # #    #      # # # # ### ##   
        #  ## ### #    ##     # # ### # # ### 
      ##                       ##             
 ___ 
|_  )  ##       #          
 / /   # # # #  #  ###  ## 
/___|o ##  # #  #  ##   #  
       # # ###  ## ### ##  
       # #                 
 ____   #       #   #  
|__ /  # # # #     ### 
 |_ \  # # # #  #   #  
|___/o  ## ###  ##  ## 
         #             
'''


SCREENS = {
    '1' : splash,
    '2' : menu,

}


def main():
    clear()
    print splash
    raw_input()
    print menu
    raw_input()
    roll_dice()
    r = Roll()
    d = r.get_new_roll()
    c = get_choice(d)
    print 'Rolled: {}'.format(' '.join(map(str,d)))
    print 'Holding: {}'.format(c)
    #p = process_single_hold(c)
    #print list(p)
    #p = process_single_hold(c)
    print 'worth: {}'.format(score_dice(c))

if __name__ == "__main__":
    main()
'''
_   ___   ____
/ | |_  ) |__ /
| |  / /   |_ \
|_| /___| |___/
               

                                        
 ##  #           #       ##             
#   ###  ## ### ###     #    ## ### ### 
 #   #  # # #    #      # # # # ### ##  
  #  ## ### #    ##     # # ### # # ### 
##                       ##             

                    
##       #          
# # # #  #  ###  ## 
##  # #  #  ##   #  
# # ###  ## ### ##  
# #                 

                
 #       #   #  
# # # #     ### 
# # # #  #   #  
 ## ###  ##  ## 
  #             

 _ 
/ |
| |
|_|
   

 ___ 
|_  )
 / / 
/___|
     

 ____
|__ /
 |_ \
|___/
     
'''
