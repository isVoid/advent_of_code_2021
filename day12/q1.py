import numpy as np

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


def find(curIdx, curPath, found, adjMat):
    if curIdx == endIdx:
        found.append(curPath[:])
        return

    for adjIdx in range(adjMat.shape[0]):
        if adjMat[curIdx, adjIdx] and not (
            vertices[adjIdx].islower() and adjIdx in curPath
        ):
            curPath.append(adjIdx)
            find(adjIdx, curPath, found, adjMat)
            curPath.pop(-1)


found = []
find(startIdx, [startIdx], found, adjMat)

print(len(found))

