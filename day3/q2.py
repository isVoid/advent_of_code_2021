from functools import reduce
from itertools import repeat


class mylist:
    def __init__(self, line):
        self._lst = list(map(lambda x: int(x), line))

    def __add__(self, other):
        return mylist([u + v for u, v in zip(self._lst, other._lst)])


def f(prev, cur):
    return prev[0] + cur[0], prev[1] + cur[1]


def break_tie(filtered, unfiltered, cur_bit, take):
    if len(filtered) == len(unfiltered) / 2:
        return list(filter(lambda x: int(x[cur_bit]) == take, unfiltered))
    return filtered


with open("sample.txt", "r") as fo:
    arr = fo.read().split()

lines, acc = reduce(f, zip(repeat(1), map(lambda x: mylist(x.strip()), arr)))
gamma = list(map(lambda x: 1 if x > lines // 2 else 0, acc._lst))
epsilon = list(map(lambda x: 1 - x, gamma))

co2, o2 = arr[:], arr[:]
cur_bit = 0
while len(co2) > 1 or len(o2) > 1:
    if len(co2) > 1:
        co2_ = list(filter(lambda x: int(x[cur_bit]) == gamma[cur_bit], co2))
        co2 = break_tie(co2_, co2, cur_bit, 1)
    if len(o2) > 1:
        o2_ = list(filter(lambda x: int(x[cur_bit]) == epsilon[cur_bit], o2))
        o2 = break_tie(o2_, o2, cur_bit, 0)
    cur_bit += 1

co2, o2 = co2[0], o2[0]

co2_10 = int(co2, 2)
o2_10 = int(o2, 2)

print(co2_10 * o2_10)

