import re
import sys

data = sys.stdin.read().strip()


def x():
    ranges = []
    toggles = []
    for line in data.splitlines():
        toggle = line.startswith('on')
        x0, x1, y0, y1, z0, z1 = list(map(int, re.findall(r'-?\d+', line)))
        ranges.append([[x0, x1 + 1], [y0, y1 + 1], [z0, z1 + 1]])
        toggles.append(toggle)
    return ranges, toggles


ranges, toggles = x()


def build_sd():
    sd = [set() for _ in range(3)]

    for i in range(3):
        for r in ranges:
            sd[i].add(r[i][0])
            sd[i].add(r[i][1])

    return list(map(sorted, sd))


sd = build_sd()

xm = {x: i for i, x in enumerate(sd[0])}
ym = {y: i for i, y in enumerate(sd[1])}
zm = {z: i for i, z in enumerate(sd[2])}

g = [[[0] * (len(sd[2]) - 1) for _ in range(len(sd[1]) - 1)] for _ in range(len(sd[0]) - 1)]

for i, (toggle, data) in enumerate(zip(toggles, ranges)):
    for x in range(xm[data[0][0]], xm[data[0][1]]):
        for y in range(ym[data[1][0]], ym[data[1][1]]):
            for z in range(zm[data[2][0]], zm[data[2][1]]):
                g[x][y][z] = toggle

t = 0
for x in range(len(g)):
    for y in range(len(g[x])):
        for z in range(len(g[x][y])):
            if g[x][y][z]:
                t += (sd[0][x + 1] - sd[0][x]) * (sd[1][y + 1] - sd[1][y]) * (sd[2][z + 1] - sd[2][z])

print(t)
