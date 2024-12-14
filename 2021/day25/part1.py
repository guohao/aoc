import itertools
import sys

data = sys.stdin.read().strip()

g = {}
for i, line in enumerate(data.splitlines()):
    for j, c in enumerate(line):
        if c != '.':
            g[i, j] = c
R = len(data.splitlines())
C = len(data.splitlines()[0])
for t in itertools.count(1):
    moved = False
    for tc, d in [('>', (0, 1)), ('v', (1, 0))]:
        ng = {}
        for p, v in g.items():
            np = (p[0] + d[0]) % R, (p[1] + d[1]) % C
            if v == tc and np not in g:
                ng[np] = v
                moved = True
            else:
                ng[p] = v
        g = ng
    if not moved:
        print(t)
        exit()
