import math
import sys

data = sys.stdin.read().strip()
ns = list(map(int, data.split(',')))

ans = math.inf
for n in range(min(ns), max(ns) + 1):
    ans = min(ans, sum(abs(x - n) for x in ns))
print(ans)