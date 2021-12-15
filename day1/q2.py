from collections import Counter

with open("../input.txt", "r") as f:
    arr = f.read().split()

prev_res = {}
def memoise(i):
    return prev_res[i] if i in prev_res else sum(int(x) for x in arr[i:i+3])
res = Counter(memoise(i) > memoise(i-1) for i in range(1, len(arr)))[True]

with open('result.txt', 'w') as f:
    f.write(str(res))