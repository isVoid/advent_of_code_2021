import numpy as np

with open("input.txt", "r") as fo:
    map_ = []
    for line in fo:
        map_.append(list(map(int, line.strip())))
arr = np.array(map_)

offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]
res = 0
for iy, ix in np.ndindex(arr.shape):
    is_minima = True
    for off in offsets:
        oy, ox = off
        adjy, adjx = iy + oy, ix + ox
        if adjy >= 0 and adjy < arr.shape[0] and adjx >= 0 and adjx < arr.shape[1]:
            is_minima &= arr[adjy, adjx] > arr[iy, ix]
    if is_minima:
        risk_level = arr[iy, ix] + 1
        res += risk_level
print(res)

