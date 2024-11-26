import sys
from collections import defaultdict

lines = sorted([line.strip() for line in sys.stdin.readlines()])
g = defaultdict(lambda: defaultdict(int))
cg = -1
ft = -1
for line in lines:
    if '#' in line:
        cg = int(line.split()[-3][1:])
    elif 'falls' in line:
        ft = line.split()[1][:-1]
    elif 'wakes' in line:
        wt = line.split()[1][:-1]
        h, m = map(int, ft.split(':'))
        if h == 23:
            m -= 60
        h2, m2 = map(int, wt.split(':'))
        if h2 == 23:
            m2 -= 60
        for i in range(m, m2):
            g[cg][i] += 1
gid = 0
mst = 0
sm = 0
for i, v in g.items():
    csm = sum(v.values())
    if csm > mst:
        gid = i
        mst = csm
        sm = max(v, key=lambda k: v[k])

print(gid * sm)
