'''
    test_gamedice_score.py
'''
from nose import tools as nt
from gamedice.scores import score_dice
from gamedice.die_utils import process_single_hold

NEED = {
    (1,1,1,1) : 2000,
    (2,2,2,2,2) : 800,
    (3,3,3,3,3,3) : 2400,
    ((4,4,4),(1,)) : 500,
    ((3,3,3),(2,2,2),(1,1),(5,)) : 750,
    ((5,5,5),(1,),(1,),(6,6,6,6)) : 1900,
    ((1,1,1,1),(2,2,2),(4,4,4,4),(1,1,1,1)) : 2600
        }

def test_3_ones():
    h = [1,1,1]
    p = process_single_hold(h)
    nt.assert_equals(1000,score_dice(p))

def test_3_twos():
    h = [2,2,2]
    p = process_single_hold(h)
    nt.assert_equals(200,score_dice(p))

def test_3_threes():
    h = [3,3,3]
    p = process_single_hold(h)
    nt.assert_equals(300,score_dice(p))

def test_3_fours():
    h = [4,4,4]
    p = process_single_hold(h)
    nt.assert_equals(400,score_dice(p))

def test_3_fives():
    h = [5,5,5]
    p = process_single_hold(h)
    nt.assert_equals(500,score_dice(p))

def test_3_sixs():
    h = [6,6,6]
    p = process_single_hold(h)
    nt.assert_equals(600,score_dice(p))

def test_doubles_without_ones_or_fives():
    h = [2,3,6,2,6,3]
    p = process_single_hold(h)
    nt.assert_equals(1000,score_dice(p))

def test_doubles_without_fives():
    h = [1,3,6,1,6,3]
    p = process_single_hold(h)
    nt.assert_equals(1000,score_dice(p))

def test_doubles_without_ones():
    h = [5,3,6,5,6,3]
    p = process_single_hold(h)
    nt.assert_equals(1000,score_dice(p))
    
def test_doubles_with_ones_and_fives():
    h = [5,1,6,5,6,1]
    p = process_single_hold(h)
    nt.assert_equals(1000,score_dice(p))

def test_four_ones():
    h = [1,1,1,1]
    p = process_single_hold(h)
    nt.assert_equals(2000,score_dice(p))


def test_five_ones():
    h = [1,1,1,1,1]
    p = process_single_hold(h)
    nt.assert_equals(4000,score_dice(p))

def test_six_ones():
    h = [1,1,1,1,1,1]
    p = process_single_hold(h)
    nt.assert_equals(8000,score_dice(p))

def test_four_twos():
    h = [2,2,2,2]
    p = process_single_hold(h)
    nt.assert_equals(400,score_dice(p))

def test_four_threes():
    h = [3,3,3,3]
    p = process_single_hold(h)
    nt.assert_equals(600,score_dice(p))

def test_four_fours():
    h = [4,4,4,4]
    p = process_single_hold(h)
    nt.assert_equals(800,score_dice(p))

def test_four_fives():
    h = [5,5,5,5]
    p = process_single_hold(h)
    nt.assert_equals(1000,score_dice(p))


def test_four_sixs():
    h = [6,6,6,6]
    p = process_single_hold(h)
    nt.assert_equals(1200,score_dice(p))

def test_five_twos():
    h = [2,2,2,2,2]
    p = process_single_hold(h)
    nt.assert_equals(800,score_dice(p))

def test_five_threes():
    h = [3,3,3,3,3]
    p = process_single_hold(h)
    nt.assert_equals(1200,score_dice(p))

def test_five_fours():
    h = [4,4,4,4,4]
    p = process_single_hold(h)
    nt.assert_equals(1600,score_dice(p))

def test_five_fives():
    h = [5,5,5,5,5]
    p = process_single_hold(h)
    nt.assert_equals(2000,score_dice(p))

def test_five_sixs():
    h = [6,6,6,6,6]
    p = process_single_hold(h)
    nt.assert_equals(2400,score_dice(p))


def test_six_twos():
    h = [2,2,2,2,2,2]
    p = process_single_hold(h)
    nt.assert_equals(1600,score_dice(p))

def test_six_threes():
    h = [3,3,3,3,3,3]
    p = process_single_hold(h)
    nt.assert_equals(2400,score_dice(p))

def test_six_fours():
    h = [4,4,4,4,4,4]
    p = process_single_hold(h)
    nt.assert_equals(3200,score_dice(p))

def test_six_fives():
    h = [5,5,5,5,5,5]
    p = process_single_hold(h)
    nt.assert_equals(4000,score_dice(p))

def test_six_sixs():
    h = [6,6,6,6,6,6]
    p = process_single_hold(h)
    nt.assert_equals(4800,score_dice(p))

def test_two_ones_and_one_five():
    h = [1,1,5]
    p = process_single_hold(h)
    nt.assert_equals(250,score_dice(p))

def test_one_one_and_two_fives():
    h = [1,5,5]
    p = process_single_hold(h)
    nt.assert_equals(200,score_dice(p))

