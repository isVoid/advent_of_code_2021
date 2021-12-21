import numpy as np

adjs = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
with open("input.txt", "r") as fo:
    x = list(map(lambda l: list(map(int, l)), fo.read().split()))
    arr = np.array(x)

zeros = np.zeros(arr.shape, dtype=int)


def step(arr):
    arr += np.ones(arr.shape, dtype=int)


def bfs(arr):
    sources = []
    for iy, ix in np.ndindex(arr.shape):
        if arr[iy, ix] > 9:
            sources.append((iy, ix))

    visited = set()
    for source in sources:
        queue = [source]
        while len(queue) > 0:
            iy, ix = queue.pop(0)
            if (iy, ix) not in visited:
                visited.add((iy, ix))
                for ox, oy in adjs:
                    iix = ix + ox
                    iiy = iy + oy
                    if (
                        iiy >= 0
                        and iiy < arr.shape[0]
                        and iix >= 0
                        and iix < arr.shape[1]
                    ):
                        arr[iiy, iix] += 1
                        if arr[iiy, iix] > 9:
                            queue.append((iiy, iix))


def discharge(arr):
    mask = arr > 9
    flashes = mask.sum()
    arr[mask] = 0
    return flashes


total = 0
for st in range(1000):
    step(arr)
    bfs(arr)
    flashes = discharge(arr)
    # total += flashes
    if flashes == arr.size:
        print(st)
        break
