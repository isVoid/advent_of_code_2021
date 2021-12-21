match = {"{": "}", "(": ")", "[": "]", "<": ">"}
scores = {")": 3, "]": 57, "}": 1197, ">": 25137}
score = 0
with open("input.txt", "r") as fo:
    for line in fo:
        stack = []
        line = line.strip()
        for c in line:
            if c in match:
                stack.append(c)
            else:
                if len(stack) == 0:
                    score += scores[c]
                    break
                else:
                    top = stack.pop(-1)
                    if match[top] != c:
                        score += scores[c]
                        break

print(score)
