import re
import sys

grid = [[0] * 1000 for _ in range(1000)]

for line in sys.stdin.readlines():
    xs, ys, xe, ye = map(int, re.findall(r'\d+', line))
    for i in range(xs, xe + 1):
        for j in range(ys, ye + 1):
            if 'turn on' in line:
                grid[i][j] += 1
            elif 'turn off' in line:
                grid[i][j] = max(0, grid[i][j] - 1)
            elif 'toggle' in line:
                grid[i][j] += 2

print(sum(sum(x) for x in grid))
