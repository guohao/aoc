import itertools
import re


def p1(data: str):
    ints = list(map(int, re.findall(r'\d+', data)))
    n = len(ints)
    seen = set()
    for t in itertools.count():
        if tuple(ints) in seen:
            return t
        seen.add(tuple(ints))
        i = [x for x in range(n) if ints[x] == max(ints)][0]
        rbt = ints[i]
        ints[i] = 0
        for j in range(rbt):
            idx = (i + j + 1) % n
            ints[idx] += 1


def p2(data: str):
    ints = list(map(int, re.findall(r'\d+', data)))
    n = len(ints)
    seen = {}
    for t in itertools.count():
        if tuple(ints) in seen:
            return t - seen[tuple(ints)]
        seen[tuple(ints)] = t
        i = [x for x in range(n) if ints[x] == max(ints)][0]
        rbt = ints[i]
        ints[i] = 0
        for j in range(rbt):
            idx = (i + j + 1) % n
            ints[idx] += 1
