import itertools
from collections import deque
from functools import reduce


def p1(data: str):
    ans = 0
    for line in data.splitlines():
        l, d = [int(x) for x in line.split(': ')]
        if l % ((d - 1) * 2) == 0:
            ans += l * d
    return ans


def p2(data: str):
    for t in itertools.count():
        caught = False
        for line in data.splitlines():
            l, d = [int(x) for x in line.split(': ')]
            if (l + t) % ((d - 1) * 2) == 0:
                caught = True
                break
        if not caught:
            return t
