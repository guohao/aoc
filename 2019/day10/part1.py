import math


def calculate_angle(center, point):
    dx = point[0] - center[0]
    dy = point[1] - center[1]
    angle = math.atan2(dy, dx)
    adjusted_angle = (angle + math.pi / 2) % (2 * math.pi)
    return adjusted_angle


import sys

data = sys.stdin.read().strip()

g = set()
for i, line in enumerate(data.splitlines()):
    for j, c in enumerate(line):
        if c == '#':
            g.add((j, i))


def count(n):
    d = set()
    for nb in g - {n}:
        d.add(calculate_angle(n, nb))
    return len(d)


print(max(count(n) for n in g))
