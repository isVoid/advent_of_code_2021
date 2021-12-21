with open("input.txt", "r") as fo:
    template = fo.readline().strip()
    fo.readline()
    rules = fo.read().split("\n")
    rules = dict(map(lambda x: x.split(" -> "), rules))

cur = {}
for a, b in zip(template[:-1], template[1:]):
    if a + b not in cur:
        cur[a + b] = 0
    cur[a + b] += 1


def step(cur):
    next_step = {}
    for k, v in cur.items():
        new_element = rules[k]
        a, b = k
        if a + new_element not in next_step:
            next_step[a + new_element] = 0
        next_step[a + new_element] += v
        if new_element + b not in next_step:
            next_step[new_element + b] = 0
        next_step[new_element + b] += v
    return next_step


def count(cur):
    counts = {}
    for k, v in cur.items():
        a, b = k
        if a not in counts:
            counts[a] = 0
        if b not in counts:
            counts[b] = 0
        counts[a] += v
        counts[b] += v

    counts[template[0]] += 1
    counts[template[-1]] += 1

    counts2 = {}
    for k, v in counts.items():
        counts2[k] = v / 2
    return counts2


for _ in range(40):
    cur = step(cur)
cnts = count(cur)
print(cnts)
vals = list(sorted(list(cnts.values())))
print(vals[-1] - vals[0])

