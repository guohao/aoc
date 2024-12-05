import re
import sys
from collections import defaultdict

g = defaultdict(int)
for line in sys.stdin.readlines():
    x1, y1, x2, y2 = list(map(int, re.findall(r'-?\d+', line)))
    x1, x2 = min(x1, x2), max(x1, x2)
    y1, y2 = min(y1, y2), max(y1, y2)
    if x1 != x2 and y1 != y2:
        continue
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            g[i, j] += 1

print(sum(v > 1 for v in g.values()))
