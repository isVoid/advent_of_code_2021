import numpy as np


class Map:
    def __init__(self, shape):
        self._arr = np.zeros(shape)

    def plot(self, line):
        # Draw the line
        sx, sy = line._start
        ex, ey = line._end

        if sx == ex:
            sy, ey = sorted((sy, ey))
            self._arr[sy : ey + 1, sx] += np.ones(ey - sy + 1)
        else:
            sx, ex = sorted((sx, ex))
            self._arr[sy, sx : ex + 1] += np.ones(ex - sx + 1)

    def count_all_overlapped_points(self):
        return (self._arr > 1).sum()


class Line:
    def __init__(self, start, end):
        self._start = start
        self._end = end

    def __repr__(self):
        return str(self._start) + "->" + str(self._end)


with open("sample.txt", "r") as fo:
    max_x, max_y = 0, 0

    lines = []
    for line in fo:
        start, end = line.strip().split(" -> ")
        start_x, start_y = start.split(",")
        end_x, end_y = end.split(",")
        start_x, start_y = int(start_x), int(start_y)
        end_x, end_y = int(end_x), int(end_y)

        max_x = max(max_x, start_x, end_x)
        max_y = max(max_y, start_y, end_y)
        if start_x == end_x or start_y == end_y:
            lines.append(Line((start_x, start_y), (end_x, end_y)))

map_ = Map((max_y + 1, max_x + 1))
for line in lines:
    map_.plot(line)
res = map_.count_all_overlapped_points()

print(map_._arr)
print(res)
