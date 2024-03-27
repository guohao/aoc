import itertools
import re
from collections import defaultdict


def p1(data: str):
    g = defaultdict(int)
    for line in data.splitlines():
        _, x, y, w, h = list(map(int, re.findall(r'\d+', line)))
        for i in range(y, y + h):
            for j in range(x, x + w):
                g[i, j] += 1
    return sum(1 for v in g.values() if v > 1)


def p2(data: str):
    g = defaultdict(int)
    for line in data.splitlines():
        _, x, y, w, h = list(map(int, re.findall(r'\d+', line)))
        for i in range(y, y + h):
            for j in range(x, x + w):
                g[i, j] += 1
    for line in data.splitlines():
        id, x, y, w, h = list(map(int, re.findall(r'\d+', line)))
        if all(g[i, j] == 1 for i, j in itertools.product(range(y, y + h), range(x, x + w))):
            return id
