import sys
from collections import deque


def solve(data:str,entry):
    ls = [l.strip() for l in data.splitlines()]
    g = {(i, j): ls[i][j] for i in range(len(ls)) for j in range(len(ls[i]))}
    visited = set()
    q = deque()
    q.append(entry)
    seen = set()
    while q:
        k = q.popleft()
        if k in seen:
            continue
        seen.add(k)
        p, (dx, dy) = k
        if p not in g:
            continue
        x, y = p
        visited.add(p)

        if g[p] == '.' or (g[p] == '|' and dy == 0) or (g[p] == '-' and dx == 0):
            q.append(((x + dx, y + dy), (dx, dy)))
        elif g[p] == '-' or g[p] == '|':
            q.append(((x - dy, y + dx), (-dy, dx)))
            q.append(((x + dy, y + dx), (dy, dx)))
            q.append(((x + dy, y - dx), (dy, -dx)))
        elif (g[p] == '/' and dx == 0) or (g[p] == '\\' and dy == 0):
            q.append(((x - dy, y + dx), (-dy, dx)))
        else:
            q.append(((x + dy, y - dx), (dy, -dx)))
    return len(visited)

print(solve(sys.stdin.read(), ((0, 0), (0, 1))))