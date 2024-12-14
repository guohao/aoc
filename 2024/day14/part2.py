import itertools
import re
import sys

X = 101
Y = 103
rs = []
for line in sys.stdin.readlines():
    p0, p1, v0, v1 = list(map(int, re.findall(r'-?\d+', line)))
    rs.append(((p0, p1), (v0, v1)))

for t in itertools.count(1):
    ns = []
    for (x, y), (dx, dy) in rs:
        nx = (x + dx) % X
        ny = (y + dy) % Y
        ns.append(((nx, ny), (dx, dy)))
    rs = ns
    g = set(r for r, v in rs)
    outs = []
    for j in range(Y):
        line = ''
        for i in range(X):
            if (i, j) in g:
                line += '#'
            else:
                line += '.'
        outs.append(line)
    if any("#########" in line for line in outs):
        print(t)
        break
