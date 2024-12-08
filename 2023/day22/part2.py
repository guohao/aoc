import re
import sys
from collections import defaultdict

bs = []
for line in sys.stdin.readlines():
    x0, y0, z0, x1, y1, z1 = list(map(int, re.findall(r'\d+', line)))
    points = []
    for x in range(x0, x1 + 1):
        for y in range(y0, y1 + 1):
            points.append((x, y))
    bs.append(((z0, z1), len(bs), points))
bs.sort()
heights = defaultdict(lambda: -1)
above = defaultdict(list)
under = defaultdict(list)
placed = []
for (z0, z1), i, points in bs:
    h = max(heights[x] for x in points)
    for (_, pz), pi, pps in placed:
        if pz == h and set(pps) & set(points):
            above[pi].append(i)
            under[i].append(pi)
    for x in points:
        heights[x] = h + z1 - z0 + 1
    placed.append(((h + 1, h + z1 - z0 + 1), i, points))
ans = 0


def bfs(deleted: set):
    nd = set()
    for d in deleted:
        for a in above[d]:
            supported = list(x for x in under[a] if x not in deleted)
            if len(supported) == 0 and a not in deleted:
                nd.add(a)
    if nd:
        return bfs(deleted.union(nd))
    else:
        return len(deleted)


for i in range(len(bs)):
    ans += bfs({i}) - 1
print(ans)
