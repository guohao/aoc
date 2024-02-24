from helper import *

data = raw_data(2017, 6)


def solve():
    banks = [int(x) for x in data.split()]
    seen = {}
    for t in itertools.count():
        if tuple(banks) in seen:
            return t, t - seen[tuple(banks)]
        seen[tuple(banks)] = t
        m = max(banks)
        i = banks.index(m)
        banks[i] = 0
        for j in range(m):
            banks[(i + 1 + j) % len(banks)] = banks[(i + 1 + j) % len(banks)] + 1


print(solve())
