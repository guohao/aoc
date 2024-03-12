import itertools
import re


def p1(data: str):
    points = []
    for line in data.splitlines():
        x, y, vx, vy = map(int, re.findall(r'-?\d+', line))
        points.append(((x, y), (vx, vy)))
    for t in itertools.count():
        G = set()
        for p in points:
            G.add(p[0])
        min_x = min(x[0][0] for x in points)
        max_x = max(x[0][0] for x in points) + 1
        min_y = min(x[0][1] for x in points)
        max_y = max(x[0][1] for x in points) + 1
        if abs(max_y - min_y) == 10:
            for y in range(min_y, max_y):
                line = ''
                for x in range(min_x, max_x):
                    if (x, y) in G:
                        line += '#'
                    else:
                        line += '.'
                print(line)
            return t
        nps = []
        for p in points:
            nps.append(((p[0][0] + p[1][0], p[0][1] + p[1][1]), p[1]))
        points = nps
