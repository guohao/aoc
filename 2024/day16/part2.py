import heapq
import math
import sys

data = sys.stdin.read().strip()
g = {(i, j): c for i, line in enumerate(data.splitlines()) for j, c in enumerate(line)}

start = next(x for x in g if g[x] == 'S')
target = next(x for x in g if g[x] == 'E')
tv = [(0, [start], (0, 1))]
SEEN = {}
best = math.inf
ans = set()
while tv:
    s, path, d = heapq.heappop(tv)
    if s > best:
        continue
    p = path[-1]
    if g.get(p, '#') == '#':
        continue
    if (p, d) in SEEN and SEEN[p, d] < s:
        continue
    SEEN[p, d] = s
    if p == target:
        best = min(best, s)
        if best == s:
            ans |= set(path)
    x, y = p
    for dx, dy in [(1, 0), (0, 1), (0, -1), (-1, 0)]:
        sa = 1 if (dx, dy) == d else 1001
        np = path + [(dx + x, dy + y)]
        heapq.heappush(tv, (s + sa, np, (dx, dy)))

print(len(ans))
