from helper import *

data = raw_data(2023, 18)
lines = lines(data)
D = {0: (0, 1), 2: (0, -1), 3: (1, 0), 1: (-1, 0)}

x = 0
y = 0
points = []

ans = 0
for line in lines:
    cmd = line.split('#')[1]
    m = int(cmd[:5], 16)
    dx, dy = D[int(cmd[5])]
    x = x + dx * m
    y = y + dy * m
    ans += m
    points.append((x, y))


def polygon_area():
    area = 0
    n = len(points)
    for i in range(n):
        j = (i + 1) % n
        area += points[i][0] * points[j][1]
        area -= points[j][0] * points[i][1]
    area = abs(area) // 2
    return area


ans = ans // 2 + polygon_area() + 1
print(ans)  #
