import itertools
import math
import re
import sys
from functools import reduce

data = sys.stdin.read().strip()

def cmp(a, b):
    return (a < b) - (a > b)


def abs_sum(l):
    return sum(abs(x) for x in l)


def ints(s: str):
    return list(map(int, re.findall(r'-?\d+', s)))


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
print(reduce(math.lcm,periods))
