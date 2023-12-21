from itertools import cycle

from helper import *

MOVES = {'<': 1, '>': 0}

data = """
>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>
"""

data = raw_data(2022, 17)
JETS = cycle(list(data.strip()))
ROCKS = cycle([
    [0b11110],
    [0b01000, 0b11100, 0b01000],
    [0b11100, 0b00100, 0b00100],
    [0b10000, 0b10000, 0b10000, 0b10000],
    [0b11000, 0b11000]
])

N = 7
G = [0] * N


def print_bin(x: List[int]):
    for i in x:
        print(bin(i)[2:].zfill(7).replace('1', '#').replace('0', '+'))


def can_move(rock, d):
    if d < 0:
        return False
    for i in range(len(rock)):
        r = rock[i]
        while r.bit_length() > 0:
            j = r.bit_length()
            if G[N - j] & 1 << (d + i):
                return False
            r &= ~(1 << j - 1)
    return True


def do_move(rock, d):
    for i in range(len(rock)):
        r = rock[i]
        while r.bit_length() > 0:
            j = r.bit_length()
            G[N - j] |= 1 << (d + i)
            r &= ~(1 << j - 1)


def create_new_rock(rock, move_left: bool):
    for i in range(len(rock)):
        if move_left and rock[i] & 1 << 6:
            return
        if not move_left and rock[i] & 1:
            return
    return [x << 1 if move_left else x >> 1 for x in rock]


ans = 0
M = 2022
for epoch in range(0, M):
    d = max(G).bit_length() + 3
    rock = next(ROCKS)
    while True:
        jet = next(JETS)
        n_r = create_new_rock(rock, MOVES[jet])
        if n_r and can_move(n_r, d):
            rock = n_r
        if can_move(rock, d - 1):
            d -= 1
        else:
            do_move(rock, d)
            break
    epoch += 1
print(max(G).bit_length())
