from collections import deque

from helper import *

data = raw_data(2023, 10)
D = {
    '-': [(0, -1), (0, 1)],
    '|': [(-1, 0), (1, 0)],
    'F': [(0, 1), (1, 0)],
    'L': [(0, 1), (-1, 0)],
    'J': [(0, -1), (-1, 0)],
    '7': [(0, -1), (1, 0)]}

lines = lines(data)
grid = grid(data)
S = (0, 0)
for p, v in grid.items():
    if v == 'S':
        S = p
        break
s_nbs = [nb for nb in neighbors_2d(grid, S) if grid[nb] != '.']
s_nbs = [nb for nb in s_nbs if S in [(nb[0] + dx, nb[1] + dy) for dx, dy in D[grid[nb]]]]
diff = [(nb[0] - S[0], nb[1] - S[1]) for nb in s_nbs]
grid[S] = [dk for dk, dv in D.items() if set(diff) == set(dv)][0]

dq = deque()
visited = set()
dq.append(S)
while dq:
    p = dq.popleft()
    if p in visited:
        continue
    visited.add(p)
    for d in D[grid[p]]:
        np = (p[0] + d[0], p[1] + d[1])
        dq.append(np)
print(len(visited) // 2)

ans = 0
for i in range(len(lines)):
    cin = False
    for j in range(len(lines[0])):
        if (i, j) in visited and grid[(i, j)] in '|7F':
            cin = not cin
        ans += (i, j) not in visited and cin
print(ans)
