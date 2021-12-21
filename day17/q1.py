import math

xrange = [209, 238]
yrange = [-86, -59]

xrange[1] += 1
yrange[1] += 1


def verify_vx0_exists(treach):
    for t in range(1, treach + 1):
        for xt in range(*xrange):
            # try 1: t <= vx0 case
            vx0 = xt / t + (t - 1) / 2
            if vx0 == int(vx0) and vx0 <= t:
                return True
            # try 2: t > vx0 case
            vx0 = math.sqrt(2 * xt)
            if vx0 == int(vx0) and vx0 > t:
                return True
    return False


for y in range(*yrange):
    treach = 2 * abs(y)
    if verify_vx0_exists(treach):
        yfound = y
        break

print((abs(yfound)) * (abs(yfound) - 1) / 2)
