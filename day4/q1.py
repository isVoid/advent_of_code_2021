import numpy as np

with open("input.txt", "r") as fo:
    nums_to_mark = list(map(int, fo.readline().strip().split(",")))
    boards = []
    num_index = {}
    for line in fo:
        if line.strip() == "":
            if num_index:
                boards.append((np.zeros(25).reshape((5, 5)), num_index))
            num_index = {}
            col, row = 0, 0
            continue
        nums = list(map(int, line.strip().split()))
        for n in nums:
            if n not in num_index:
                num_index[n] = set()
            num_index[n].add((row, col))
            col += 1

        col = 0
        row += 1
    boards.append((np.zeros(25).reshape((5, 5)), num_index))


def win(board):
    # row-wise
    if board.all(axis=1).any():
        return True
    # col-wise
    if board.all(axis=0).any():
        return True
    return False


res = None
for n in nums_to_mark:
    for pair in boards:
        board, num_index = pair
        if n in num_index:
            coords = num_index[n]
            for coord in coords:
                board[coord] = 1
            num_index.pop(n)

            if win(board):
                res = sum(k * len(v) for k, v in num_index.items()) * n
                break
    if res:
        break

print(res)
