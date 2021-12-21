def visualize(points):
    from functools import reduce
    import numpy as np

    np.set_printoptions(linewidth=np.inf)

    max_x, max_y = reduce(
        lambda p, c: Point(
            (max(p._coord[0], c._coord[0]), max(p._coord[1], c._coord[1]))
        ),
        points,
    )._coord

    arr = np.zeros((max_y + 1, max_x + 1), dtype=object)
    for p in points:
        x, y = p._coord
        arr[y, x] = 1

    arr[arr == 0] = "."
    arr[arr == 1] = "#"

    print(arr)


class Point:
    def __init__(self, coord):
        self._coord = coord

    def _fold_along_axis0(self, axis):
        # fold along x == 0 or y == 0
        x, y = self._coord
        if axis == "x":
            return Point((-x, y))
        else:
            return Point((x, -y))

    def _shift(self, axis, by):
        x, y = self._coord
        if axis == "x":
            return Point((x + by, y))
        else:
            return Point((x, y + by))

    def fold_along_any_axis(self, fold):
        x, y = self._coord
        axis, n = fold
        # Assuming an exact fold
        if axis == "x" and x < n:
            return self
        if axis == "y" and y < n:
            return self

        return self._shift(axis, -n)._fold_along_axis0(axis)._shift(axis, n)

    def __repr__(self):
        return str(self._coord)

    # The below are required for hashable types

    def __hash__(self):
        return self._coord.__hash__()

    def __eq__(self, other):
        return self._coord == other._coord


fn = "input"

with open(f"{fn}.txt", "r") as fo:
    # I moved all folds to a separate file.
    lines = fo.read().split()
    dots = set(map(lambda x: Point(tuple(map(int, x.split(",")))), lines))


def line_processor(line):
    axis, num = line.split("=")
    num = int(num)
    return axis, num


with open(f"{fn}_folds.txt", "r") as fo:
    # This file looks like:
    # y=7
    # x=5
    # ...
    lines = fo.read().split()
    folds = list(map(line_processor, lines))


for f in folds:
    # print(len(dots))
    dots = set(map(lambda d: d.fold_along_any_axis(f), dots))

# print(len(dots))
visualize(dots)

