import numpy as np
from itertools import count
import heapq
from dataclasses import dataclass, field


def is_valid(point, arr):
    x, y = point._coord
    return x >= 0 and x < arr.shape[1] and y >= 0 and y < arr.shape[0]


class Point:
    def __init__(self, x, y):
        self._coord = (x, y)

    def __add__(self, other):
        x0, y0 = self._coord
        x1, y1 = other._coord
        return Point((x0 + x1), (y0 + y1))

    def __eq__(self, other):
        return self._coord == other._coord

    def __hash__(self):
        return self._coord.__hash__()

    def __repr__(self):
        return str(self._coord)

    def adjNodes(self, arr):
        for d in directions:
            adj = self + d
            if is_valid(adj, arr):
                yield adj


P = Point

directions = [P(-1, 0), P(1, 0), P(0, -1), P(0, 1)]

# Helper for priority queue to compare only with risk level but also
# carries the main record
@dataclass(order=True)
class Item:
    risk: int
    p: Point = field(compare=False)


with open("input.txt", "r") as fo:
    vals = list(map(lambda row: list(map(int, row)), fo.read().split()))
    arr = np.array(vals)


pq = []

risk = {}
for y, x in np.ndindex(arr.shape):
    risk[P(x, y)] = np.inf
risk[P(0, 0)] = 0

visited = set()
cost = 0

heapq.heappush(pq, Item(0, P(0, 0)))
while pq:
    it = heapq.heappop(pq)
    cur = it.p
    for adj in cur.adjNodes(arr):
        if adj not in visited:
            adj_risk = risk[cur] + arr[adj._coord]
            if adj_risk < risk[adj]:
                risk[adj] = adj_risk
                heapq.heappush(pq, Item(adj_risk, adj))
    visited.add(cur)

print(risk[P(99, 99)])
