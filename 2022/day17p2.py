from itertools import cycle

from helper import *

MOVES = {'<': 1, '>': 0}

data = """
>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>
"""

data = raw_data(2022, 17)
JETS = cycle(list(data.strip()))
ROCKS = cycle([[0b11110],
               [0b01000, 0b11100, 0b01000],
               [0b11100, 0b00100, 0b00100],
               [0b10000, 0b10000, 0b10000, 0b10000],
               [0b11000, 0b11000]
               ])

G = [0 for _ in range(30)]


def print_bin(x: List[int]):
    for i in x:
        print(bin(i)[2:].zfill(7))


def can_move_down(rock, d):
    if d < 0:
        return False
    for i in range(len(rock)):
        if G[d + i] & rock[i]:
            return False
    return True


def do_move(rock, d):
    for i in range(len(rock)):
        G[d + i] |= rock[i]


def create_new_rock(rock, move_left: bool):
    print(f'creating new rock with move {"left" if move_left else "right"}')
    for i in range(len(rock)):
        if move_left and rock[i] & 1 << 6:
            return
        if not move_left and rock[i] & 1:
            return
    return [x << 1 if move_left else x >> 1 for x in rock]


def clean_prev(n):
    for i in range(n):
        G[i] = 0
    for i in range(n, len(G)):
        G[i - n] = G[i]

epoch = 0
ans = 0
while epoch < 4:
    for i, line in enumerate(G):
        if line == 0:
            d = i + 3
            if d > 20:
                clean_prev(10)
                d -= 10
            print(f'start new epoch {epoch} from {d}')
            if epoch == 2024:
                print(i)
            break
    rock = next(ROCKS)
    while True:
        jet = next(JETS)
        n_r = create_new_rock(rock, MOVES[jet])
        print(f'rock is ready to move {jet}')
        print_bin(rock)
        if n_r:
            print(f'new rock is created after move {jet}')
            print_bin(n_r)
            rock = n_r
        else:
            print(f'cannot move {jet}')
        if can_move_down(rock, d - 1):
            print(f'can move down {d - 1}')
            d -= 1
        else:
            print(f'can not move down {d - 1}, do move down {d}')
            do_move(rock, d)
            break
    epoch += 1
print_bin(G)
