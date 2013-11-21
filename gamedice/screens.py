#encoding:UTF-8
'''
    screens.py
'''
#__all__ = [splash]
import os

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

def main():
    clear()
    print splash
    raw_input()

if __name__ == "__main__":
    main()
