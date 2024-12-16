import heapq
import sys

data = sys.stdin.read().strip()
g = {(i, j): c for i, line in enumerate(data.splitlines()) for j, c in enumerate(line)}

start = next(x for x in g if g[x] == 'S')
target = next(x for x in g if g[x] == 'E')
tv = [(0, start, (0, 1))]
SEEN = set()
while tv:
    s, p, d = heapq.heappop(tv)
    if g.get(p, '#') == '#':
        continue
    if (p, d) in SEEN:
        continue
    SEEN.add((p, d))
    if p == target:
        print(s)
        break
    x, y = p
    for dx, dy in [(1, 0), (0, 1), (0, -1), (-1, 0)]:
        sa = 1 if (dx, dy) == d else 1001
        heapq.heappush(tv, (s + sa, (dx + x, dy + y), (dx, dy)))
