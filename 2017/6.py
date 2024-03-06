import itertools


def p1(data: str):
    banks = [int(x) for x in data.split()]
    seen = {}
    for t in itertools.count():
        if tuple(banks) in seen:
            return t
        seen[tuple(banks)] = t
        m = max(banks)
        i = banks.index(m)
        banks[i] = 0
        for j in range(m):
            banks[(i + 1 + j) % len(banks)] = banks[(i + 1 + j) % len(banks)] + 1


def p2(data: str):
    banks = [int(x) for x in data.split()]
    seen = {}
    for t in itertools.count():
        if tuple(banks) in seen:
            return t - seen[tuple(banks)]
        seen[tuple(banks)] = t
        m = max(banks)
        i = banks.index(m)
        banks[i] = 0
        for j in range(m):
            banks[(i + 1 + j) % len(banks)] = banks[(i + 1 + j) % len(banks)] + 1
