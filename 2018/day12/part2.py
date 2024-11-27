import sys
from itertools import count

lines = [line.strip() for line in sys.stdin.readlines()]
d = {a: b for a, b in zip(count(), lines[0].split()[-1])}
ts = {l: r for l, r in map(lambda x: x.split(' => '), lines[2:]) if r == '#'}


def snapshot():
    return sorted([i - min(d) for i in range(min(d), max(d) + 1) if i in d])


for k in count():
    s0 = snapshot()
    nd = {}
    for i in range(min(d) - 4, max(d) + 4):
        p = ''.join(d.get(j, '.') for j in range(i - 2, i + 3))
        if p in ts:
            nd[i] = ts[p]
    d = nd
    s1 = snapshot()
    if s0 == s1:
        print(sum(snapshot()) + (50000000000 - k + min(d) - 1) * len(d))
        break
