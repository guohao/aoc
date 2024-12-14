import sys
from collections import Counter, defaultdict

data = sys.stdin.read().strip()

parts = data.split('\n\n')
s = parts[0]
ms = {}
for line in parts[1].splitlines():
    l, r = line.split(' -> ')
    ms[l] = r
g = defaultdict(int)
for i in range(1, len(s)):
    pair = s[i - 1:i + 1]
    g[pair] += 1
c = Counter(s)
for _ in range(40):
    ng = defaultdict(int)
    for k, v in g.items():
        if k in ms:
            c[ms[k]] += v
            ng[k[0] + ms[k]] += v
            ng[ms[k] + k[1]] += v
    g = ng

c = sorted(c.values())
print(c[-1] - c[0])
