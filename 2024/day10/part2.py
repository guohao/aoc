import sys
from collections import deque, defaultdict

ls = [l.strip() for l in sys.stdin.readlines()]
g = defaultdict(str) | {(i, j): ls[i][j] for i in range(len(ls)) for j in range(len(ls[i]))}
t = 0

q = deque()
starts = [x for x in g if g[x] == '0']
for s in starts:
    q.append((s, s))
t = 0
while q:
    s, p = q.popleft()
    if g[p] == '9':
        t+=1
        continue
    x, y = p
    for dx, dy in [(1, 0), (0, 1), (0, -1), (-1, 0)]:
        nx, ny = x + dx, y + dy
        if g[nx, ny] == str(int(g[p]) + 1):
            q.append((s, (nx, ny)))

print(t)
