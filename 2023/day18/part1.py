import math
import sys


def polygon_area(vertices):
    n = len(vertices)
    area = 0
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]
        area += x1 * y2 - y1 * x2
    return abs(area) / 2


def boundary_points(vertices):
    n = len(vertices)
    boundary_points = 0
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]
        boundary_points += math.gcd(abs(x2 - x1), abs(y2 - y1))
    return boundary_points


def internal_points(vertices):
    return polygon_area(vertices) - boundary_points(vertices) / 2 + 1


def total_points(vertices):
    return int(internal_points(vertices) + boundary_points(vertices))


vs = [(0, 0)]
DS = {
    'R': (0, 1),
    'L': (0, -1),
    'U': (-1, 0),
    'D': (1, 0)
}
for line in sys.stdin.readlines():
    d, n, _ = line.split()
    n = int(n)
    d = DS[d]
    vs.append((vs[-1][0] + d[0] * n, vs[-1][1] + d[1] * n))
print(total_points(vs))
