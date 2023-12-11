import itertools

from common import io_utils

data = io_utils.get_data(2023, 11)
lines = data.strip().splitlines()
wx = [1] * len(lines[0])
wy = [1] * len(lines[0])


def cal(w):
    for i, line in enumerate(lines):
        if sum(1 for x in line if x == '.') == len(line):
            wx[i] = w
    for i in range(len(lines[0])):
        if sum(lines[j][i] == '.' for j in range(len(lines))) == len(lines):
            for j in range(len(lines)):
                wy[i] = w

    grid = {(i, j): lines[i][j] for i, j in itertools.product(range(len(lines)), range(len(lines[0])))}

    ss = [(i, j) for i, j in grid.keys() if grid[i, j] == '#']

    ans = 0
    for p in ss:
        r = ss.copy()
        r.remove(p)
        for p2 in r:
            ans += sum(wx[i] for i in range(min(p[0], p2[0]), max(p[0], p2[0])))
            ans += sum(wy[i] for i in range(min(p[1], p2[1]), max(p[1], p2[1])))

    print(ans // 2)


cal(2)
cal(1000000)
