import heapq
import itertools
import string
from collections import deque
from functools import cache


#     G = nx.Graph()
#     start = None
#     for i, line in enumerate(data.splitlines()):
#         for j, c in enumerate(line):
#             if c == '@':
#                 start = i, j
#             if c != '#':
#                 G.add_node((i, j), v=c)
#
#     q = [(0, start, frozenset())]
#     seen = set()
#     while q:
#         steps, p, keys = heapq.heappop(q)
#         if len(keys) == len(string.ascii_lowercase):
#             return steps
#         if (p, keys) in seen:
#             continue
#         seen.add((p, keys))
#         for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
#             np = p[0] + dx, p[1] + dy
#             if np in G:
#                 c: string = G.nodes[np]['v']
#                 if c.isupper() and c.lower() not in keys:
#                     continue
#                 if c.islower():
#                     q.append((steps + 1, np, keys | frozenset([c])))
#                 else:
#                     q.append((steps + 1, np, keys))

def solve(data: str, is_p2):
    G = {}
    start = None
    for i, line in enumerate(data.splitlines()):
        for j, c in enumerate(line):
            if c == '@':
                start = i, j
            if c != '#':
                G[i, j] = c
    starts = []
    if is_p2:
        for i, j in itertools.product(range(-1, 2), repeat=2):
            nb = start[0] + i, start[1] + j
            if abs(i) + abs(j) < 2:
                G[nb] = '#'
            else:
                G[nb] = '@'
                starts.append(nb)
    else:
        starts = [start]

    @cache
    def reachable(cx, cy, keys):
        rq = deque([(cx, cy, 0)])
        visited = set()
        while rq:
            cx, cy, moved = rq.popleft()

            if G[cx, cy].islower() and G[cx, cy] not in keys:
                yield cx, cy, moved
                continue
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                np = cx + dx, cy + dy
                if np in G:
                    if np in visited:
                        continue
                    visited.add(np)
                    if G[np].isupper() and G[np].lower() not in keys:
                        continue
                    rq.append((*np, moved + 1))

    q = [(0, tuple(starts), frozenset())]
    seen = set()
    while q:
        steps, ps, keys = heapq.heappop(q)
        if len(keys) == len(string.ascii_lowercase):
            return steps
        if (ps, keys) in seen:
            continue
        seen.add((ps, keys))
        for i, p in enumerate(ps):
            for x, y, distance in reachable(*p, keys):
                nps = ps[:i] + ((x, y),) + ps[i + 1:]
                heapq.heappush(q, (steps + distance, tuple(nps), keys | frozenset([G[x, y]])))


import sys
data = sys.stdin.read().strip()

    return solve(data, False)


import sys
data = sys.stdin.read().strip()

    return solve(data, True)
