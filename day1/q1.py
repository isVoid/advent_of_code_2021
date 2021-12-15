from collections import Counter
with open("../input.txt", "r") as f:
    arr = f.read().split()
res = Counter(int(cur) > int(prev) for prev, cur in zip(arr[:-1], arr[1:]))[True]

with open("result.txt", "w") as f:
    f.write(str(res))