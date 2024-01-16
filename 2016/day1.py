from helper import *

data = raw_data(2016, 1)

x, y = 0, 0
face = (-1, 0)
visited = set()
found = False
for move in data.strip().split(', '):
    d, n = move[0], int(move[1:])
    if d == 'R':
        face = (face[1], -face[0])
    else:
        face = (-face[1], face[0])
    for i in range(n):
        x += face[0]
        y += face[1]
        if (x, y) in visited and not found:
            print('p2', abs(x) + abs(y))
            found = True
        visited.add((x, y))
print(abs(x) + abs(y))
