import re

import io_utils

data = io_utils.get_data(2022, 8)
grid = [list(map(int, re.findall(r'\d', line))) for line in data.strip().splitlines()]
ans = 0
for i, line in enumerate(grid):
    for j, h in enumerate(line):
        ts = [[grid[i][x] for x in range(j - 1, -1, -1)],
              [grid[i][x] for x in range(j + 1, len(grid[0]))],
              [grid[x][j] for x in range(i - 1, -1, -1)],
              [grid[x][j] for x in range(i + 1, len(grid))]
              ]
        if len(ts) < 4:
            continue
        ss = 1
        for t in ts:
            vc = 0
            for oh in t:
                vc += 1
                if oh >= h:
                    break
            ss = ss * vc
        ans = max(ans, ss)

print(ans)
