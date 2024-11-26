import itertools
import sys
from collections import defaultdict

lines = [line.strip() for line in sys.stdin.readlines()]
g = defaultdict(int)
for line in lines:
    import re

    i, l, t, w, h = list(map(int, re.findall(r'-?\d+', line)))
    for j in range(l, l + w):
        for k in range(t, t + h):
            g[j, k] += 1

for line in lines:
    i, l, t, w, h = list(map(int, re.findall(r'-?\d+', line)))
    if all(g[j, k] == 1 for j, k in itertools.product(range(l, l + w), range(t, t + h))):
        print(i)
        break
