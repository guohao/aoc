from collections import deque

from helper import *

data = raw_data(2023, 18)
lines = lines(data)
g = {}
D = {'R': (0, 1), 'L': (0, -1), 'U': (1, 0), 'D': (-1, 0)}

SX, SY = math.inf, math.inf
EX, EY = -math.inf, -math.inf
x = 0
y = 0
for line in lines:
    d, m, _ = line.split()
    m = int(m)
    dx, dy = D[d]
    for _ in range(m):
        x = x + dx
        SX = min(SX, x)
        SY = min(SY, y)
        EX = max(EX, x)
        EY = max(EY, y)
        y = y + dy
        g[x, y] = d

V = set()
dq = deque()
for i in range(SX, EX + 1):
    if (i, SY) not in g:
        dq.append((i, SY))
    if (i, EY) not in g:
        dq.append((i, EY))
for j in range(SY, EY + 1):
    if (SX, j) not in g:
        dq.append((SX, j))
    if (EX, j) not in g:
        dq.append((EX, j))
while dq:
    x, y = dq.popleft()
    if (x, y) in V:
        continue
    V.add((x, y))
    for dx, dy in D.values():
        nx = x + dx
        ny = y + dy
        if (nx, ny) not in g and nx in range(SX, EX + 1) and ny in range(SY, EY + 1):
            dq.append((nx, ny))

print((EX - SX + 1) * (EY - SY + 1) - len(V))
