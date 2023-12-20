from functools import cache

import nographs as nog
from helper import *

data = raw_data(2023, 17)
D = frozenset([(0, 1), (1, 0), (0, -1), (-1, 0)])


def next_edges(state: tuple[int, int, int, tuple[int, int]], _):
    x, y, c, d = state

    nd = D.copy() - {(-d[0], -d[1])}
    if c == 3:
        nd = nd - {d}
    for dx, dy in nd:
        nc = c + 1 if (dx, dy) == d else 1
        nx = x + dx
        ny = y + dy
        if 0 <= nx < N and 0 <= ny < M:
            yield (nx, ny, nc, (dx, dy)), g[nx, ny]


lines = data.strip().splitlines()
N = len(lines)
M = len(lines[0])
g = {i[0]: int(i[1]) for i in grid_dict(lines).items()}
trav = nog.TraversalShortestPaths(next_edges)
ans = math.inf

for c, d in itertools.product(range(1, 4), D - {(-1, 0), (0, -1)}):
    v = trav.start_from((0, 0, 1, (0, 0)), build_paths=True).go_to((N - 1, M - 1, c, d))
    ans = min(ans, trav.distance)
print(ans)