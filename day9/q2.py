import numpy as np

with open("input.txt", "r") as fo:
    map_ = []
    for line in fo:
        map_.append(list(map(int, line.strip())))
arr = np.array(map_)

offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]
minimas = set()
for iy, ix in np.ndindex(arr.shape):
    is_minima = True
    for off in offsets:
        oy, ox = off
        adjy, adjx = iy + oy, ix + ox
        if adjy >= 0 and adjy < arr.shape[0] and adjx >= 0 and adjx < arr.shape[1]:
            is_minima &= arr[adjy, adjx] > arr[iy, ix]
    if is_minima:
        minimas.add((iy, ix))


def bfs(minima, arr):
    visited = set()
    offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    to_visit = [minima]

    while to_visit:
        iy, ix = to_visit.pop(0)
        visited.add((iy, ix))
        for off in offsets:
            oy, ox = off
            adjy, adjx = iy + oy, ix + ox
            if (
                adjy >= 0
                and adjy < arr.shape[0]
                and adjx >= 0
                and adjx < arr.shape[1]
                and (adjy, adjx) not in visited
                and arr[adjy, adjx] < 9
            ):
                to_visit.append((adjy, adjx))
    return len(visited)


sizes = []
for minima in minimas:
    size = bfs(minima, arr)
    sizes.append(size)

sizes = sorted(sizes, reverse=True)
print(sizes[0] * sizes[1] * sizes[2])

