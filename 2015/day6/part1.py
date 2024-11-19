import re

grid = [[0] * 1000 for _ in range(1000)]
try:
    while True:
        cmd = input()
        xs, ys, xe, ye = map(int, re.findall(r'\d+', cmd))
        for i in range(xs, xe + 1):
            for j in range(ys, ye + 1):
                if 'turn on' in cmd:
                    grid[i][j] = 1
                elif 'turn off' in cmd:
                    grid[i][j] = 0
                elif 'toggle' in cmd:
                    grid[i][j] = 1 - grid[i][j]
except EOFError:
    print(sum(sum(x) for x in grid))
