from itertools import repeat

with open("input.txt", "r") as fo:
    arr = fo.read().split()


def count_pos_and_lines(arr):
    pos_counts = None
    for line in arr:
        if pos_counts is None:
            pos_counts = dict(zip(range(len(line.strip())), repeat(0)))
        for i, s in enumerate(line.strip()):
            pos_counts[i] += int(s)
    return pos_counts, len(arr)


def compute_gamma_epsilon(pos_counts, lines):
    gamma, epsilon = "", ""
    for v in pos_counts.values():
        if v > lines / 2:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"
    return gamma, epsilon


# Compute o2
cur = arr[:]
cur_bit = 0
while len(cur) > 1:
    pos_counts, lines = count_pos_and_lines(cur)
    gamma, _ = compute_gamma_epsilon(pos_counts, lines)
    buf = []
    buf_comp = []
    for line in cur:
        if line[cur_bit] == gamma[cur_bit]:
            buf.append(line)
        else:
            buf_comp.append(line)
    if 2 * len(buf) == len(cur):
        # keep ones
        if gamma[cur_bit] == "1":
            cur = buf
        else:
            cur = buf_comp
    else:
        cur = buf
    cur_bit += 1

o2 = cur[0]

# Compute co2
cur = arr[:]
cur_bit = 0
while len(cur) > 1:
    pos_counts, lines = count_pos_and_lines(cur)
    _, epsilon = compute_gamma_epsilon(pos_counts, lines)
    buf = []
    buf_comp = []
    for line in cur:
        if line[cur_bit] == epsilon[cur_bit]:
            buf.append(line)
        else:
            buf_comp.append(line)
    if 2 * len(buf) == len(cur):
        # keep ones
        if gamma[cur_bit] == "0":
            cur = buf
        else:
            cur = buf_comp
    else:
        cur = buf
    cur_bit += 1

co2 = cur[0]

print(int(o2, 2) * int(co2, 2))
