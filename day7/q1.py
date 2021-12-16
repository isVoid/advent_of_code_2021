with open("input.txt", "r") as fo:
    arr = list(map(int, fo.read().strip().split(",")))


def crab_fuel(n):
    return (1 + n) * n // 2


def calc(arr, pos):
    # q1
    # return sum(map(lambda x: abs(x - pos), arr))
    # q2
    return sum(map(lambda x: crab_fuel(abs(x - pos)), arr))


def diff_at(arr, pos):
    return calc(arr, pos) - calc(arr, pos - 1)


start, end = 0, max(arr) - 1
while abs(start - end) > 1:
    mid = (start + end) // 2
    diff_mid = diff_at(arr, mid)

    if diff_mid > 0:
        end = mid
    elif diff_mid < 0:
        start = mid
    else:
        raise ValueError()

print(start, calc(arr, start))
