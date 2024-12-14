import math

import sys
from collections import deque

data = sys.stdin.read().strip()

g = set()
for i, line in enumerate(data.splitlines()):
    for j, c in enumerate(line):
        if c == '#':
            g.add((j, i))

X, Y = 23, 20


def dis_of(x0, y0):
    return calculate_angle((X, Y), (x0, y0)), abs(X - x0) + abs(Y - y0)


def calculate_angle(center, point):
    dx = point[0] - center[0]
    dy = point[1] - center[1]
    angle = math.atan2(dy, dx)
    adjusted_angle = (angle + math.pi / 2) % (2 * math.pi)
    return adjusted_angle


nbs = list(g - {(X, Y)})
nbs.sort(key=lambda x: dis_of(x[0], x[1]))
q = deque(nbs)
x, y = 0, 0
for _ in range(200):
    x, y = q.popleft()
    last = dis_of(x, y)[0]
    while dis_of(*q[0])[0] == last:
        q.rotate(-1)
print(100 * x + y)
