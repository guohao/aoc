import itertools
import math
import sys
import re

lines = [line.strip() for line in sys.stdin.readlines()]
ps = []
for line in lines:
    nums = list(map(int, re.findall(r'-?\d+', line)))
    ps.append(nums)


def dist(k):
    a = trans(k)
    x0, x1, y0, y1 = range_of(a)
    return abs(x1 - x0) + abs(y1 - y0)


def range_of(a):
    x0 = y0 = math.inf
    x1 = y1 = -math.inf
    for v in a:
        x0 = min(x0, v[0])
        x1 = max(x1, v[0])
        y0 = min(y0, v[1])
        y1 = max(y1, v[1])
    return x0, x1, y0, y1


def trans(k):
    na = []
    for p in ps:
        na.append((p[0] + k * p[2], p[1] + k * p[3]))
    return na


for i in itertools.count():
    if dist(i) < 80:
        print(i)
        break
