from itertools import cycle

from helper import *

MOVES = {'<': (0, -1), '>': (0, 1), 'D': (-1, 0), "N": (0, 0)}

data = """
>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>
"""

data = raw_data(2022, 17)
JETS = cycle(list(data.strip()))
ROCKS = cycle([[[1, 1, 1, 1]],
               [[0, 1, 0],
                [1, 1, 1],
                [0, 1, 0]],
               [[1, 1, 1],
                [0, 0, 1],
                [0, 0, 1]],
               [[1], [1], [1], [1]],
               [[1, 1], [1, 1]]
               ])

G = [[0 for _ in range(7)] for _ in range(5000)]


def can_move(rock, move, l, d):
    for i in range(len(rock)):
        for j in range(len(rock[0])):
            if rock[i][j] == 0:
                continue
            if d + i + move[0] < 0 or d + i + move[0] >= len(G) or l + j + move[1] < 0 or l + j + move[1] >= len(G[0]):
                return False
            if G[d + i + move[0]][l + j + move[1]]:
                return False
    return True


def do_move(rock, move, l, d):
    for i in range(len(rock)):
        for j in range(len(rock[0])):
            if rock[i][j] == 0:
                continue
            x = d + i + move[0]
            y = l + j + move[1]
            G[x][y] = 1


epoch = 1
while epoch < 2024:
    epoch += 1
    for i, line in enumerate(G):
        if sum(line) == 0:
            d = i + 3
            if epoch == 2024:
                print(i)
            break
    rock = next(ROCKS)
    l = 2
    while True:
        jet = next(JETS)
        if can_move(rock, MOVES[jet], l, d):
            l += MOVES[jet][1]
        if can_move(rock, MOVES['D'], l, d):
            d -= 1
        else:
            do_move(rock, MOVES['N'], l, d)
            break
# print_lines(G)
