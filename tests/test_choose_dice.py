'''
    test_choose_dice.py
'''
from gamedice.choose_dice import get_choice
import nose.tools as nt


need = ([1,1,1,1,1,1],[3,3,3,4,4,6],[4,4,4,4,6,6],[5,5,5,5,5,4],[6,6,6,6,6,6],[2,2,3,3,4,4],[1,1,3,3,4,4],[3,3,5,5,4,4],[1,1,5,5,4,4],[1,2,3,4,5,6],[5,5,4,1,6,1],[3,3,3,1,1,4],[3,3,3,1,1,5],[4,4,4,4,1,6],[4,4,4,4,1,5]) 
def test_six_ones():
    nt.assert_equals((1,1,1,1,1,1),get_choice(need[0])[0])

def test_three_of_a_kind():
    nt.assert_equals((3,3,3),get_choice(need[1])[0])

def test_four_of_a_kind():
    nt.assert_equals((4,4,4,4),get_choice(need[2])[0])

def test_five_of_a_kind():
    nt.assert_equals((5,5,5,5,5),get_choice(need[3])[0])

def test_six_of_a_kind():
    nt.assert_equals((6,6,6,6,6,6),get_choice(need[4])[0])

def test_doubles_no_ones_or_fives():
    nt.assert_equals((2,2,3,3,4,4),get_choice(need[5])[0])

def test_doubles_with_ones_no_fives():
    nt.assert_equals((1,1,3,3,4,4),get_choice(need[6])[0])

def test_doubles_with_no_ones_with_fives():
    nt.assert_equals((3,3,5,5,4,4),get_choice(need[7])[0])

def test_doubles_with_ones_and_fives():
    nt.assert_equals((1,1,5,5,4,4),get_choice(need[8])[0])

def test_strait():
    nt.assert_equals((1,2,3,4,5,6),get_choice(need[9])[0])

def test_two_ones_and_two_fives():
    nt.assert_equals([(1,1),(5,5)],get_choice(need[10]))

def test_three_of_a_kind_and_two_ones():
    nt.assert_equals([(3,3,3),(1,1)],get_choice(need[11]))

def test_three_of_a_kind_and_two_ones_and_a_five():
    nt.assert_equals([(3,3,3),(1,1),(5,)],get_choice(need[12]))

def test_four_of_a_kind_with_one():
    nt.assert_equals([(4,4,4,4),(1,)],get_choice(need[13]))

def test_four_of_a_kind_with_one_and_five():
    nt.assert_equals([(4,4,4,4),(1,),(5,)],get_choice(need[14]))
     
if __name__ == "__main__":
    from nose import main
    main()
