# coding: utf-8
def split_nums(nums):
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
    rtn = []
    for itm in d:
        rtn.append(tuple(((itm+' ')*int(d[itm])).split()))
    return tuple(rtn)

def main():
    n = [1,5,1,6,6,5,6]
    print split_nums(n)[:-1] + get_t_from_d(split_nums(n)[2])

if __name__ == "__main__":
    main()
