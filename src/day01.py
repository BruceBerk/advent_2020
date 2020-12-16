import itertools
import numpy as np


def find_sum_2020(infile: str) -> int:
    """Read a sequence of numbers, find the pair whose sum is 2020 and return their product"""

    lower_half = []
    upper_half = []
    mid_count = 0

    with open(infile) as inf:
        content = inf.read().splitlines()
        for line in content:
            num = int(line)
            if num == 1010:
                mid_count += 1
            elif num < 1010:
                lower_half.append(num)
            else:
                upper_half.append(num)

    if mid_count >= 2:
        return 1010 * 1010
    else:
        for l in lower_half:
            for u in upper_half:
                if (l + u) == 2020:
                    return l * u

    return 0


def find_triple_sum(infile: str):
    """Find 3 numbers in the series whose sum is 2020 - return their product"""
    numlist = []
    with open(infile) as inf:
        content = inf.read().splitlines()
        for line in content:
            numlist.append(int(line))

    combos = list(itertools.combinations(numlist, 3))
    solut = [c for c in combos if sum(c) == 2020]
    return np.prod(solut)


ans = find_sum_2020('../data/test01.txt')
print(f'test answer is {ans}')

ans = find_sum_2020('../data/input01.txt')
print(f'real answer is {ans}')

ans = find_triple_sum('../data/test01.txt')
print(f'test answer is {ans}')

ans = find_triple_sum('../data/input01.txt')
print(f'real answer is {ans}')
