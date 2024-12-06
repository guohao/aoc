import itertools
import sys
from collections import deque

lines = [l.strip() for l in sys.stdin.readlines()]
og = {(i, j): lines[i][j] for i, j in itertools.product(range(len(lines)), range(len(lines[0])))}

t = 0
for k in og:
    if og[k] in '^#':
        continue
    g = og.copy()
    g[k] = '#'
    start = [k for k, v in g.items() if v == '^'][0]
    q = deque()
    q.append([start, (-1, 0)])
    seen = set()
    while q:
        (x, y), (dx, dy) = q.popleft()
        k = ((x, y), (dx, dy))
        if k in seen:
            t += 1
            break
        seen.add(k)
        nx, ny = x + dx, y + dy
        if (nx, ny) not in g:
            break
        if g[nx, ny] == '#':
            dx, dy = dy, -dx
            nx, ny = x + dx, y + dy
            if (nx, ny) not in g:
                break
            elif g[nx, ny] == '#':
                dx, dy = dy, -dx
                nx, ny = x + dx, y + dy
                if (nx, ny) not in g:
                    break
        q.append(((nx, ny), (dx, dy)))
print(t)
