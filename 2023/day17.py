from heapq import *

from helper import *

lines = lines(raw_data(2023, 17))
GOAL = (len(lines) - 1, len(lines[0]) - 1)

g = {}
for i, line in enumerate(lines):
    for j, c in enumerate(line):
        g[i, j] = int(c)


def dfs(min_step, max_step) -> int:
    pq = [(0, (0, 0), (0, 0), min_step)]
    visited = set()
    while pq:
        heat_lost, p, d, step = heappop(pq)
        if (p, d, step) in visited:
            continue
        visited.add((p, d, step))
        if p == GOAL:
            print(heat_lost)
            return
        for nd in {(1, 0), (0, 1), (0, -1), (-1, 0)} - {(-d[0], -d[1])}:
            if d == nd and step == max_step:
                continue
            if d != nd and step < min_step:
                continue
            ns = step + 1 if d == nd else 1
            np = (p[0] + nd[0], p[1] + nd[1])
            if np in g:
                heappush(pq, (heat_lost + g[np], np, nd, ns))


dfs(1, 3)
dfs(4, 10)
