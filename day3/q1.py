from functools import reduce
from itertools import repeat

class mylist:
    def __init__ (self, line):
        self._lst = list(map(lambda x: int(x), line))
    def __add__(self, other):
        return mylist([u + v for u, v in zip(self._lst, other._lst)])

def f(prev, cur):
    return prev[0] + cur[0], prev[1] + cur[1]

lines, acc = reduce(f, zip(repeat(1), map(lambda x: mylist(x.strip()), open('input.txt', 'r'))))

gamma = list(map(lambda x: 1 if x > lines // 2 else 0, acc._lst))
epsilon = list(map(lambda x: 1 - x, gamma))

# convert base 2 to base 10
res_a = reduce(lambda prev, cur: (prev[0] + cur[0] * 2**cur[1], prev[1]), zip(reversed(gamma), range(len(gamma))))
res_b = reduce(lambda prev, cur: (prev[0] + cur[0] * 2**cur[1], prev[1]), zip(reversed(epsilon), range(len(epsilon))))

with open('q1.txt', 'w') as f:
    f.write(str(res_a[0] * res_b[0]))