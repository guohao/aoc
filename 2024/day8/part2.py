import sys
from collections import defaultdict
from itertools import product

ls = [l.strip() for l in sys.stdin.readlines()]
X = len(ls)
Y = len(ls[0])

gd = defaultdict(list)
for i in range(len(ls)):
    for j in range(len(ls[i])):
        v = ls[i][j]
        if v != '.':
            gd[v].append((i, j))
ans = set()
for k, v in gd.items():
    for a, b in product(v, repeat=2):
        if a == b:
            continue
        x = 2 * a[0] - b[0]
        y = 2 * a[1] - b[1]
        ans.add(a)
        while 0 <= x < X and 0 <= y < Y:
            ans.add((x, y))
            x += a[0] - b[0]
            y += a[1] - b[1]

print(len(ans))
