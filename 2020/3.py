import math


def p1(data: str):
    g = {}
    lines = data.splitlines()
    n = len(lines)
    m = len(lines[0])
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            g[i, j] = c
    ans = 0
    j = 0
    for i in range(n):
        if g[i, j] == '#':
            ans += 1
        j = (j + 3) % m
    return ans


def p2(data: str):
    g = {}
    lines = data.splitlines()
    n = len(lines)
    m = len(lines[0])
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            g[i, j] = c

    def solpe(x, y):
        ans = 0
        i = j = 0
        while i < n:
            if g[i, j] == '#':
                ans += 1
            j = (j + y) % m
            i += x
        return ans

    return math.prod(solpe(y, x) for x, y in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)])

