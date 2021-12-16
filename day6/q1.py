from collections import Counter
from itertools import repeat, chain, islice

# Requires python 3.7+
def left_shift_dict_values(old_d):
    new_d = dict(
        zip(
            range(9),
            chain(
                islice(old_d.values(), 1, 7), [old_d[0] + old_d[7], old_d[8], old_d[0]]
            ),
        )
    )
    return new_d


with open("input.txt", "r") as fo:
    arr = list(map(int, fo.read().split(",")))
d = dict(zip(range(9), repeat(0)))
d.update(Counter(arr))

days = 256
for _ in range(days):
    d = left_shift_dict_values(d)

print(d)
print(sum(d.values()))
