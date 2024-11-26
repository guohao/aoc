import sys
import re
from collections import defaultdict

lines = [line.strip() for line in sys.stdin.readlines()]
g = defaultdict(int)
for line in lines:

    i, l, t, w, h = list(map(int, re.findall(r'-?\d+', line)))
    for j in range(l, l + w):
        for k in range(t, t + h):
            g[j, k] += 1
print(sum(v > 1 for v in g.values()))
