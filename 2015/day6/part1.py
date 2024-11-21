import re

grid = [[0] * 1000 for _ in range(1000)]
import sys

lines = sys.stdin.readlines()
for line in lines:
    xs, ys, xe, ye = map(int, re.findall(r'\d+', line))
    for i in range(xs, xe + 1):
        for j in range(ys, ye + 1):
            if 'turn on' in line:
                grid[i][j] = 1
            elif 'turn off' in line:
                grid[i][j] = 0
            elif 'toggle' in line:
                grid[i][j] = 1 - grid[i][j]
print(sum(sum(x) for x in grid))
