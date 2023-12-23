from itertools import cycle

from helper import *

MOVES = {'<': 1, '>': 0}

data = """
>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>
"""

data = raw_data(2022, 17)
JETS = cycle(list(data.strip()))
ROCKS = cycle([
    [1, 1, 1, 1],
    [3, 7, 3],
    [1, 1, 7],
    [15],
    [3, 3]
])

N = 7
G = [0] * N


def print_bin(x: List[int]):
    for i in x:
        print(bin(i)[2:].zfill(7).replace('1', '#').replace('0', '+'))


def can_move(rock, left, down):
    if down < 0:
        return False
    if left < 0 or left + len(rock) >= N:
        return False
    for j in range(len(rock)):
        if G[left + j] & (rock[j] << down):
            return False
    return True


def do_move(rock, left, down):
    for j in range(len(rock)):
        G[left + j] |= rock[j] << down


def p(epoch):
    for _ in range(0, epoch):
        down = max(G).bit_length() + 3
        rock = next(ROCKS)
        left = 2
        while True:
            move = MOVES[next(JETS)]
            if can_move(rock, left + move, down):
                left += move
            if can_move(rock, left, down - 1):
                down -= 1
            else:
                do_move(rock, left, down)
                break


p(1)
print_bin(G)
print(max(G).bit_length())
