import re
import sys

data = sys.stdin.read()
maze, path = data.split('\n\n')
if maze[0] == '\n':
    maze = maze[1:]
path = 'R' + path

g = {(i, j): c for i, line in enumerate(maze.splitlines()) for j, c in enumerate(line) if c != ' '}
limits = (min(x for x, _ in g), max(x for x, _ in g), min(y for _, y in g), max(y for _, y in g))
N = limits[1] - limits[0] + 1
M = limits[3] - limits[2] + 1


def neighbor(p, facing) -> (int, int):
    assert p
    limit = N if facing[0] != 0 else M
    for _ in range(limit):
        np = ((p[0] + facing[0]) % N, (p[1] + facing[1]) % M)
        if np in g:
            if g[np] == '.':
                return np
            elif g[np] == '#':
                return None
        p = np


p = (0, maze.index('.'))
facing = (-1, 0)
for move in re.findall(r'[RL]\d+', path):
    steps = int(move[1:])
    direction = move[0]
    if direction == 'R':
        facing = (facing[1], -facing[0])
    else:
        facing = (-facing[1], facing[0])
    for i in range(steps):
        np = neighbor(p, facing)
        if np:
            p = np
        else:
            break

ans = 1000 * (p[0] + 1) + 4 * (p[1] + 1)
match facing:
    case (0, 1):
        ans += 0
    case (1, 0):
        ans += 1
    case (0, -1):
        ans += 2
    case (-1, 0):
        ans += 3
print(ans)
