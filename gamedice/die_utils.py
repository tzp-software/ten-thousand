# coding: utf-8
'''
    dicelib.die_utils.py
'''
import os
import sys

def clear():
    #x = os.system('clear')
    x = '\n\n'*100
    #os.write(sys.stdout, x)
    print x
    
def split_nums(nums):
    ''' split a tuple into seperate tuples of each number
        ie:         split_nums((2,3,4,2,3,5)) 
        returns:    (2,2),(3,3),(4,),(5,)
    '''
    ones = []
    fives = []
    others = {}
    for n in nums:
        if str(n) == '1':
            ones.append(n)
        elif str(n) == '5':
            fives.append(n)
        else:
            if others.get(str(n)):
                others[str(n)] += 1
            else:
                others[str(n)] = 1
    return (tuple(ones),tuple(fives),others)

def get_tuple_from_count_dict(d):
    '''
        given a dict of {num:count} 
        returns a tuple of (num*count)
        if count = 5
        returns (num,num,num,num,num)
    '''
    rtn = []
    for itm in d:
        rtn.append(tuple(((itm+' ')*int(d[itm])).split()))
    return tuple(rtn)

def main():
    n = [1,5,1,6,6,5,6]
    print split_nums(n)[:-1] + get_t_from_d(split_nums(n)[2])

if __name__ == "__main__":
    main()
