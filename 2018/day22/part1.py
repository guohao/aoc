import re
import sys

import networkx as nx


def ints(line):
    return list(map(int, re.findall(r'-?\d+', line)))


def build_g(depth, target):
    g = {}
    X, Y = target[0] + 100, target[1] + 100
    for i in range(1, X + 1):
        g[i, 0] = (depth + (i * 16807)) % 20183
    for j in range(1, Y + 1):
        g[0, j] = (depth + (j * 48271)) % 20183
    g[0, 0] = depth % 20183
    g[target] = depth % 20183
    for j in range(1, Y + 1):
        for i in range(1, X + 1):
            if (i, j) == target:
                continue
            g[i, j] = (depth + (g[i - 1, j] * g[i, j - 1])) % 20183
    return {k: v % 3 for k, v in g.items()}



data = sys.stdin.read()
lines = data.splitlines()
depth = ints(lines[0])[0]
target = tuple(ints(lines[1]))
g = build_g(depth, target)
print(sum(v for k, v in g.items() if k[0] <= target[0] and k[1] <= target[1]))


def p2(data: str):
    lines = data.splitlines()
    depth = ints(lines[0])[0]
    target = tuple(ints(lines[1]))
