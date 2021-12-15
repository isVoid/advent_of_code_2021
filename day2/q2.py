from functools import reduce
with open('input.txt', 'r') as f:
    inputs = f.read().split()

def f(cnt, x):
    direction, distance = x
    distance = int(distance)
    if direction == 'forward':
        cnt['horizontal'] += distance
        cnt['vertical'] += cnt['aim'] * distance
    elif direction == 'down':
        cnt['aim'] += distance
    elif direction == 'up':
        cnt['aim'] -= distance
    else:
        raise ValueError(f'Unrecognized direction {direction}.')
    return cnt
counts = reduce(f, zip(inputs[::2], inputs[1::2]), {'horizontal': 0, 'vertical': 0, 'aim': 0})

with open('q2.txt', 'w') as f:
    f.write(str(counts['horizontal'] * counts['vertical']))