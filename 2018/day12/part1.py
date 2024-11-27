import sys
from itertools import count

lines = [line.strip() for line in sys.stdin.readlines()]
d = {a: b for a, b in zip(count(), lines[0].split()[-1])}
ts = {l: r for l, r in map(lambda x: x.split(' => '), lines[2:]) if r == '#'}

for _ in range(20):
    nd = {}
    for i in range(min(d) - 4, max(d) + 4):
        p = ''.join(d.get(j, '.') for j in range(i - 2, i + 3))
        if p in ts:
            nd[i] = ts[p]
    d = nd

print(sum(d))
