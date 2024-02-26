from collections import defaultdict

from helper import *

data = raw_data(2017, 8)


def solve():
    r = defaultdict(int)
    max_v = 0
    for line in lines(data):
        v0, op0, c0, _, v1, op1, c1 = line.split()
        c0 = int(c0)
        c1 = int(c1)
        v1 = r[v1]
        if eval(f'{v1} {op1} {c1}'):
            if op0 == 'inc':
                r[v0] += int(c0)
            else:
                r[v0] -= int(c0)
        max_v = max(max_v, r[v0])
    return max(r.values()), max_v


print(solve())
