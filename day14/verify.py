from collections import Counter

with open("sample_res.txt", "r") as fo:
    for line in fo:
        print(Counter(line.strip()))
        print(len(line.strip()))
