import numpy as np
from itertools import repeat

with open("input.txt", "r") as fo:
    l = fo.read().split()
    vertices = dict()
    for path in l:
        v0, v1 = path.split("-")
        if v0 not in vertices:
            vertices[v0] = None
        if v1 not in vertices:
            vertices[v1] = None
    adjMat = np.zeros((len(vertices), len(vertices)), dtype=bool)
    vertices = list(vertices.keys())
    for path in l:
        v0, v1 = path.split("-")
        iv0 = vertices.index(v0)
        iv1 = vertices.index(v1)
        adjMat[iv0, iv1] = True
        adjMat[iv1, iv0] = True

startIdx = vertices.index("start")
endIdx = vertices.index("end")


def find(curIdx, curPath, found, count, adjMat, picked):
    if curIdx == endIdx:
        found.append(curPath[:])
        return

    for adjIdx in range(adjMat.shape[0]):
        if (
            adjMat[curIdx, adjIdx]
            and not adjIdx == startIdx
            and (
                vertices[adjIdx].isupper()
                or (vertices[adjIdx].islower() and count[adjIdx] == 0)
                or (vertices[adjIdx].islower() and count[adjIdx] == 1 and not picked)
            )
        ):
            if vertices[adjIdx].islower() and count[adjIdx] == 1 and not picked:
                picked = True
            curPath.append(adjIdx)
            count[adjIdx] += 1
            find(adjIdx, curPath, found, count, adjMat, picked)
            curPath.pop(-1)
            count[adjIdx] -= 1
            if vertices[adjIdx].islower() and count[adjIdx] == 1 and picked:
                picked = False


found = []
find(
    startIdx,
    [startIdx],
    found,
    dict(zip(range(len(vertices)), repeat(0))),
    adjMat,
    False,
)

# for f in found:
#     print(list(map(vertices.__getitem__, f)))

print(len(found))

