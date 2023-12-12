from helper import *

data = raw_data(2023, 11)
lines = data.strip().splitlines()
wx = [1] * len(lines[0])
wy = [1] * len(lines[0])


def cal(w):
    for i, line in enumerate(lines):
        if line.count('.') == len(line):
            wx[i] = w
    for i in range(len(lines[0])):
        if sum(lines[j][i] == '.' for j in range(len(lines))) == len(lines):
            for j in range(len(lines)):
                wy[i] = w

    grid = grid_dict(lines)

    ss = grid_find(grid, '#')

    ans = 0
    for p in ss:
        for p2 in ss:
            ans += sum(wx[i] for i in range(min(p[0], p2[0]), max(p[0], p2[0])))
            ans += sum(wy[i] for i in range(min(p[1], p2[1]), max(p[1], p2[1])))

    print(ans // 2)


cal(2)
cal(1000000)
