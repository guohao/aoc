from collections import deque

from helper import *

data = raw_data(2022, 12)

lines = lines(data)
grid = grid_dict(lines)
start = grid_find_first(grid, 'S')
grid[start] = 'a'
stop = grid_find_first(grid, 'E')
grid[stop] = 'z'
ds = {stop: 0}

v = deque([stop])
while v:
    p = v.popleft()
    for x in grid_find_4_neighbors(grid, p):
        if x not in ds and ord(grid[p]) <= ord(grid[x]) + 1:
            ds[x] = ds[p] + 1
            v.append(x)

print(min(d[1] for d in ds.items() if grid[d[0]] == 'a'))
