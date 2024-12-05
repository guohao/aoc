import itertools
import sys
import heapq

lines = [line.strip() for line in sys.stdin.readlines()]
g = {(i, j): int(lines[i][j]) for i, j in itertools.product(range(len(lines)), range(len(lines[0])))}
heap = [(0, (1, 0), (1, 0), 1), (0, (0, 1), (0, 1), 1)]
heapq.heapify(heap)
seen = set()
target = max(g)
while heap:
    cost, (x, y), (dx, dy), moved = heapq.heappop(heap)
    if moved == 4:
        continue
    if (x, y) not in g:
        continue
    cost += g[x, y]
    k = ((x, y), (dx, dy), moved)
    if k in seen:
        continue
    seen.add(k)
    if (x, y) == target:
        print(cost)
        break
    for nx, ny in [(-dy, dx), (dy, -dx), (dx, dy)]:
        n_move = 1 if (nx, ny) != (dx, dy) else (moved + 1)
        heapq.heappush(heap, (cost, (x + nx, y + ny), (nx, ny), n_move))
