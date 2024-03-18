import re


def ints(line):
    return list(map(int, re.findall(r'-?\d+', line)))


def p1(data: str):
    lines = data.splitlines()
    depth = ints(lines[0])[0]
    X, Y = tuple(ints(lines[1]))
    g = {}
    for i in range(1, X + 1):
        g[i, 0] = (depth + (i * 16807)) % 20183
    for j in range(1, Y + 1):
        g[0, j] = (depth + (j * 48271)) % 20183
    for i in range(1, X + 1):
        for j in range(1, Y + 1):
            g[i, j] = (depth + (g[i - 1, j] * g[i, j - 1])) % 20183
    g[X, Y] = depth % 20183
    g[0, 0] = depth % 20183
    return sum(v % 3 for v in g.values())
