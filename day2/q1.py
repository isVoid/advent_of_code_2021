from functools import reduce
with open('input.txt', 'r') as f:
    inputs = f.read().split()

def f(cnt, x):
    direction, distance = x
    if direction == 'forward':
        cnt['horizontal'] += int(distance)
    elif direction == 'down':
        cnt['vertical'] += int(distance)
    elif direction == 'up':
        cnt['vertical'] -= int(distance)
    else:
        raise ValueError(f'Unrecognized direction {direction}.')
    return cnt
counts = reduce(f, zip(inputs[::2], inputs[1::2]), {'horizontal': 0, 'vertical': 0})

with open('q1.txt', 'w') as f:
    f.write(str(counts['horizontal'] * counts['vertical']))