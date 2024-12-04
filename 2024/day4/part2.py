import sys
import itertools
from collections import Counter

ls = [l.strip() for l in sys.stdin.readlines()]
g = {(i, j): ls[i][j] for i in range(len(ls)) for j in range(len(ls[i]))}
t = 0
for i, j in itertools.product(range(len(ls)), range(len(ls[0]))):
    if g[i, j] != 'A':
        continue
    nbs = {(a, b): g.get((i + a, j + b), '') for a, b in [(-1, -1), (-1, 1), (1, 1), (1, -1)]}
    c = Counter(nbs.values())
    if c['S'] == c['M'] == 2 and nbs[-1, -1] != nbs[1, 1]:
        t += 1
print(t)
