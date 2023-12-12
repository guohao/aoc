from collections import deque

from helper import *

data = raw_data(2022, 12)

lines = lines(data)
grid = grid_dict(lines)
start = grid_find_first(grid, 'S')
grid[start] = 'a'
stop = grid_find_first(grid, 'E')
grid[stop] = 'z'
ds = {start: 0}

v = deque()
v.append(start)
while v:
    p = v.popleft()
    for x in grid_find_4_neighbors(grid, p):
        if x not in ds and ord(grid[p]) + 1 >= ord(grid[x]):
            ds[x] = ds[p] + 1
            v.append(x)

print(ds[stop])
