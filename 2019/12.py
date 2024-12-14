import itertools
import math
import re


def cmp(a, b):
    return (a < b) - (a > b)


def abs_sum(l):
    return sum(abs(x) for x in l)




def ints(s: str):
    return list(map(int, re.findall(r'-?\d+', s)))


import sys
data = sys.stdin.read().strip()

    moons = []
    for i, line in enumerate(data.splitlines()):
        moons.append([i] + ints(line) + [0, 0, 0])
    for _ in range(1000):
        for ma in moons:
            n = ma[0]
            for mb in moons[:n] + moons[n + 1:]:
                for i in range(3):
                    ma[4 + i] += cmp(ma[1 + i], mb[1 + i])
        for ma in moons:
            for i in range(3):
                ma[i + 1] += ma[i + 4]
    return sum(abs_sum(m[1:4]) * abs_sum(m[4:7]) for m in moons)


import sys
data = sys.stdin.read().strip()

    dims = [[] for _ in range(3)]
    for line in data.splitlines():
        for i in range(3):
            dims[i].append([ints(line)[i]] + [0])

    periods = []
    for i in range(3):
        dim = dims[i]
        cmp_state = [x.copy() for x in dim]
        for t in itertools.count():
            for ma, mb in itertools.combinations(dim, 2):
                ma[1] += cmp(ma[0], mb[0])
                mb[1] += cmp(mb[0], ma[0])
            for ma in dim:
                ma[0] += ma[1]
            if cmp_state == dim:
                periods.append(t + 1)
                break
    return lcm(periods)
