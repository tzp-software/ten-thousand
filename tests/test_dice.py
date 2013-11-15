'''
    test_dice.py
'''
from nose.tools import *
from gamedice.dice import Roll


# testing Roll.hold_choice() function
class TestDiceHoldChoiceClass(object):
    def setup(self):
        self.roll = Roll()
        self.roll.get_new_roll()

    def tear_down(self):
        self.roll = ''

    def test_one_back_two_given(self):
        choice = [(1,1,1,1),(5,)]
        self.roll.hold_dice(choice)
        assert_equals(1,len(self.roll))

    def test_one_back_three_given(self):
        choice = [(1,),(5,),(3,3,3)]
        self.roll.hold_dice(choice)
        assert_equals(1,len(self.roll))

    def test_two_back_one_given(self):
        choice = [(5,5,5,5)]
        self.roll.hold_dice(choice)
        assert_equals(2,len(self.roll))

    def test_three_back_one_given(self):
        choice = [(3,3,3)]
        self.roll.hold_dice(choice)
        assert_equals(3,len(self.roll))


if __name__ == "__main__":
    from nose import main
    main()
