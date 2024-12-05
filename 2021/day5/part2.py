import re
import sys
from collections import defaultdict

g = defaultdict(int)
for line in sys.stdin.readlines():
    x1, y1, x2, y2 = list(map(int, re.findall(r'-?\d+', line)))
    dx = (x2 - x1) // abs(x1 - x2) if x2 != x1 else 0
    dy = (y2 - y1) // abs(y1 - y2) if y2 != y1 else 0
    if x1 != x2 and y1 != y2:
        if abs(y2 - y1) != abs(x2 - x1):
            continue
    while True:
        g[x1, y1] += 1
        if x1 == x2 and y1 == y2:
            break
        x1 += dx
        y1 += dy

print(sum(v > 1 for v in g.values()))
