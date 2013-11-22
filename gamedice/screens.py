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


HELD = []
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

rolled = '''
          _     
\_/_     |_) _ || _  _|o 
 |(_)|_| | \(_)||(/_(_|o 

{}\n{}\n{}
|_|o.__|_ o 
| ||| ||_ o {}    
\    /_ .__|_|_  o 
 \/\/(_)|  |_| | o {}
    press enter to keep the hint
    or type num enter to keep the 
    dice under num
'''

D1 = '''
  ###    
   ##    
   ##    
   ##    
 ######  
'''

D2 = '''
 ####### 
      ## 
 ####### 
 ##      
 ####### 
'''

D3 = '''
 ####### 
      ## 
    #### 
      ## 
 ####### 
'''

D4 = '''
 ##      
 ##  ##  
 ####### 
     ##  
     ##  
'''

D5 = '''
 ####### 
 ##      
 ####### 
      ## 
 ####### 
'''

D6 = '''####### 
 ##      
 # ##### 
 ##   ## 
 ####### 
'''
def is_held(die):
    global HELD
    if len(HELD) > 0:
        for itm in HELD:
            if not itm.id == die.id:
                HELD.append(die)
                return False
    return True

def print_rolled(dice):
    holds = [' {} ']*len(dice)
    for d in range(len(dice)):
        if is_held(dice[d]):
            holds[d] = holds[d].format('held')
    f = Figlet(font='future_8')
    dies = f.renderText(' '.join(map(str,dice)))
    labels = ('  ({})  ' + '   ')*len(dice)
    hint = get_choice(dice)
    score = score_dice(hint)
    clear()
    print rolled.format(labels.format(*range(1,len(dice)+1)),dies,holds,hint,score)

SCREENS = {
    '1' : splash,
    '2' : menu,
    '3' : rolled,
}


def main():
    clear()
    print splash
    raw_input()
    clear()
    print menu
    raw_input()
    clear()
    roll_dice()
    r = Roll()
    d = r.get_new_roll()
    c = get_choice(d)
    print_rolled(d)
    #print 'Holding: {}'.format(c)
    #p = process_single_hold(c)
    #print list(p)
    #p = process_single_hold(c)
    #print 'worth: {}'.format(score_dice(c))

if __name__ == "__main__":
    main()
    #from dice import Roll
    #print_rolled(Roll().get_new_roll())
'''print 
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
     

          _     
\_/_     |_) _ || _  _|o 
 |(_)|_| | \(_)||(/_(_|o 
                         

                                                          
                                                          
  ###     #######   #######   ##        #######   ####### 
   ##          ##        ##   ##  ##    ##        ##      
   ##     #######      ####   #######   #######   # ##### 
   ##     ##             ##       ##         ##   ##   ## 
 ######   #######   #######       ##    #######   ####### 
                                                          

         
         
  ###    
   ##    
   ##    
   ##    
 ######  
         

         
         
 ####### 
      ## 
 ####### 
 ##      
 ####### 
         

         
         
 ####### 
      ## 
    #### 
      ## 
 ####### 
         

         
         
 ##      
 ##  ##  
 ####### 
     ##  
     ##  
         

         
         
 ####### 
 ##      
 ####### 
      ## 
 ####### 
         

         
         
 ####### 
 ##      
 # ##### 
 ##   ## 
 ####### 
        

            
|_|o.__|_ o 
| ||| ||_ o 
            

                   
\    /_ .__|_|_  o 
 \/\/(_)|  |_| | o 
                   
'''
