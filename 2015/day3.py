from helper import *

data = raw_data(2015, 3)

p = (0, 0)
visited = {p}

DIRECTIONS = {'^': (-1, 0), '>': (0, 1), '<': (0, -1), 'v': (1, 0)}
for step in data.strip():
    dx, dy = DIRECTIONS[step]
    p = (dx + p[0], dy + p[1])
    visited.add(p)
print(len(visited))

visited.clear()
s = (0, 0)
r = (0, 0)
for ss, sr in zip(data[::2], data[1::2]):
    dx, dy = DIRECTIONS[ss]
    s = (dx + s[0], dy + s[1])
    visited.add(s)
    dx, dy = DIRECTIONS[sr]
    r = (dx + r[0], dy + r[1])
    visited.add(r)
print(len(visited))
