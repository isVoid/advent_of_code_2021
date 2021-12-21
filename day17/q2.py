import math

# xrange = [20, 30]
# yrange = [-10, -5]

xrange = [209, 238]
yrange = [-86, -59]

xrange[1] += 1
yrange[1] += 1


def find_vx0(treach):
    # Similar to how to search vy0, besides xt is a piecewise function
    # xt = vx0*t - t*(t - 1) / 2        (t <= vx0)
    # xt = (vx0 - 1) ^ 2 / 2            (t > vx0)

    possible_vx0 = []
    for xt in range(*xrange):
        # try 1: t <= vx0 case
        vx0 = xt / treach + (treach - 1) / 2
        if vx0 == int(vx0) and treach <= vx0:
            possible_vx0.append(vx0)
        # try 2: t > vx0 case
        vx0 = (
            math.sqrt(2 * xt) - 0.5
        )  # this estimates argmax_x0(xt), then check if any of the side satisfies.
        vx0a = math.ceil(vx0)
        vx0b = math.floor(vx0)
        for vx0 in [vx0a, vx0b]:
            if xt == vx0 * vx0 - 0.5 * vx0 * (vx0 - 1) and treach > vx0:
                possible_vx0.append(vx0)
    return possible_vx0


# yt = vy0*t - t*(t - 1) / 2
#   => vy0 = yt / t - t*(t - 1) / 2
# Search within integer space, for all valid (yt, t) combination,
# find integral vy0.
#
# Then, for given t, invoke find_vx0 to find integral vx0 similarly.
#
# The upper bound of t is basically trail and error, increment tmax
# exponentially until valid_combos doesn't increase.
valid_combo = set()
for y in range(*yrange):
    for treach in range(1, 512):
        vy0 = y / treach + (treach - 1) / 2
        if vy0 == int(vy0):
            possible_vx0 = find_vx0(treach)
            for vx0 in possible_vx0:
                valid_combo.add((int(vx0), int(vy0)))

# print(list(sorted(valid_combo)))
print(len(valid_combo))
