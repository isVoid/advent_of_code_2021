match = {"{": "}", "(": ")", "[": "]", "<": ">"}
scores = {")": 1, "]": 2, "}": 3, ">": 4}
all_scores = []
with open("input.txt", "r") as fo:
    for line in fo:
        stack = []
        line = line.strip()
        corrupted = False
        for c in line:
            if c in match:
                stack.append(c)
            else:
                if len(stack) == 0:
                    corrupted = True
                    break
                else:
                    top = stack.pop(-1)
                    if match[top] != c:
                        corrupted = True
                        break
        if not corrupted:
            score = 0
            for c in reversed(stack):
                comp = match[c]
                score = score * 5 + scores[comp]
            all_scores.append(score)

all_scores = sorted(all_scores)
print(all_scores[len(all_scores) // 2])

