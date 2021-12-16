with open("input.txt", "r") as fo:
    patterns = []
    digits = []
    for line in fo:
        p, d = line.split("|")
        patterns.append(p.split())
        digits.append(d.split())

cnt = 0
for ds in digits:
    for d in ds:
        if len(d) == 2 or len(d) == 3 or len(d) == 4 or len(d) == 7:
            cnt += 1

print(cnt)
