import re
from collections import Counter

n = 2503
dist = [[] for _ in range(n)]

import sys

lines = [line.strip() for line in sys.stdin.readlines()]
for line in lines:
    s, d, r = map(int, re.findall(r'\d+', line))
    for i in range(n):
        dist[i].append(((i + 1) // (d + r) * d + min(d, (i + 1) % (d + r))) * s)

c = Counter()
for i in range(n):
    for j in range(len(dist[i])):
        if dist[i][j] == max(dist[i]):
            c[j] += 1
print(c.most_common()[0][1])
