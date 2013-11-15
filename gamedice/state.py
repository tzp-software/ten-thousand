'''
    gamedice.state.py

    generic state class
'''
import random

class State(object):
    _stateCount = 0
    _stateList = [][:]
    _currentState = None
    
    def __init__(self,stateInfo):
        self.idx = State._stateCount
        State._stateCount += 1
        self.stateNum = State._stateCount
        self.stateName = 'State{}'.format(self.stateNum)
        self.id = stateInfo
        self.score = 0
        State._stateList.append(self)
        if State._currentState is None:
            State.set_current(self)
        self.id = stateInfo
        
    
    def __str__(self):
        #rtn = 'State for {}'.format(self.info['name'])
        return repr(self)

    def __repr__(self):
        return self.stateName

    def set_score(self,score):
        self.score += score
        
    @staticmethod
    def get_current():
        return State._currentState

    @staticmethod
    def set_current(state):
        State._currentState = state

    @staticmethod
    def set_random():
        State.set_current(random.choice(State._stateList))


    def change_state(self):
        if self.idx == len(State._stateList)-1:
            State.set_current(State._stateList[0])
        else:
            State.set_current(State._stateList[self.stateNum])

def main():
    s1, s2, s3, s4 = State(''),State(''),State(''),State('')
    count = 10
    while count > 0:
        current = State.get_current()
        print current
        raw_input()
        current.change_state()
        count -= 1

if __name__ == "__main__":
    main()
