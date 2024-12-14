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
print(sum(abs_sum(m[1:4]) * abs_sum(m[4:7]) for m in moons))
