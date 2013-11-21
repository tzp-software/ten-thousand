
from scores import get_counts, score_dice, get_score
from die_utils import split_nums, get_tuple_from_count_dict


class Scorer(object):
    def _process_dice(self,dice):
        return split_nums(dice)[:-1] + get_tuple_from_count_dict(split_nums(dice)[2])

    def get_score(self, dice):
        #combos = self._process_dice(dice)
        return score_dice(dice)

if __name__ == "__main__":
    held = [1,1,4,4,4,6,6,6,5,1,5,2,2,2]
    scorer = Scorer()
    print 'Roll: {}'.format(' '.join(map(str,held)))
    print 'Score: {}'.format(scorer.get_score(held))
