import re

from helper import *

data = """
        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5
"""
data = raw_data(2022, 22)
maze, path = data.split('\n\n')
if maze[0] == '\n':
    maze = maze[1:]
path = 'R' + path

g = {}


def parse_input():
    for i, line in enumerate(maze.splitlines()):
        for j, c in enumerate(line):
            if c != ' ':
                g[(i, j)] = c


parse_input()
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


def solve():
    p = (0, maze.index('.'))
    facing = (-1, 0)
    for move in re.findall(r'[RL]\d+', path):

        print(move)
        steps = int(move[1:])
        direction = move[0]
        if direction == 'R':
            facing = (facing[1], -facing[0])
        else:
            facing = (-facing[1], facing[0])
        for i in range(steps):
            # if facing == (0, 1):
            #     g[p] = '>'
            # elif facing == (1, 0):
            #     g[p] = 'v'
            # elif facing == (0, -1):
            #     g[p] = '<'
            # else:
            #     g[p] = '^'
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
    # print(facing)
    print(p)
    print(ans)
    return


solve()

# for i in range(N):
#     line = ''
#     for j in range(M):
#         if (i, j) in g:
#             line += g[i, j]
#         else:
#             line += ' '
#     print(line)
