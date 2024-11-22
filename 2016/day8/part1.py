import itertools
import re
import sys

R = 6
C = 50
g = [['.'] * C for _ in range(R)]
lines = [line.strip() for line in sys.stdin.readlines()]
for line in lines:
    pos, offset = list(map(int, re.findall(r'-?\d+', line)))
    if 'rect' in line:
        for i, j in itertools.product(range(offset), range(pos)):
            g[i][j] = '#'
    elif 'row' in line:
        pos %= R
        g[pos] = g[pos][-offset:] + g[pos][:-offset]
    elif 'column' in line:
        pos %= C
        col = [g[i][pos] for i in range(R)]
        col = col[-offset:] + col[:-offset]
        for i in range(R):
            g[i][pos] = col[i]

print(sum(a.count('#') for a in g))
