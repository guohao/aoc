from collections import deque

import nographs as nog
from helper import *

data = raw_data(2023, 21)
lines = lines(data.strip())
g = nog.Array(lines, 2)
H = len(lines)


def bfs(start, steps):
    dq = deque()
    dq.append({start})
    const_num = [0, 0]
    mem = deque(maxlen=2)
    mem.append(set())
    mem.append(set())
    ax = [0, 0, 0]
    for i in range(1, steps + 1):
        points = dq.popleft()
        next_visit = set()
        visited = mem.popleft()
        for point in points:
            for neighbor in point.neighbors(nog.Position.moves(2)):
                if neighbor in visited:
                    continue
                wrap = neighbor.wrap_to_cuboid(g.limits())
                if g[wrap] != "#":
                    next_visit.add(neighbor)
        const_num[i % 2] += len(visited)
        mem.append(next_visit)
        dq.append(next_visit)
        if i % H == steps % H:
            ax[i // H] = len(next_visit) + const_num[i % 2]
            if ax[2] != 0:
                break
    n = steps // H
    a = (ax[2] + ax[0] - 2 * ax[1]) / 2
    b = ax[1] - ax[0] - a
    c = ax[0]

    return int(a * n ** 2 + b * n + c)


S = g.findall('S')[0]
print(bfs(S, 64))
print(bfs(S, 26501365))
