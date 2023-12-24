from itertools import cycle

from helper import *

MOVES = {'<': -1, '>': 1}

data = """
>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>
"""

# data = raw_data(2022, 17)
JETS = cycle(list(data.strip()))
ROCKS = cycle([
    [1, 1, 1, 1],
    [2, 7, 2],
    [1, 1, 7],
    [15],
    [3, 3]
])

N = 7
G = [0] * N


def print_bin(x: List[int]):
    for n in range(max(x).bit_length() - 1, -1, -1):
        print(''.join(['#' if (i >> n) & 1 else '.' for i in x]))


def can_move(rock, left, down):
    if down < 0:
        return False
    if left < 0 or left + len(rock) > N:
        return False
    for j in range(len(rock)):
        if G[left + j] & (rock[j] << down):
            return False
    return True


def do_move(rock, left, down):
    for j in range(len(rock)):
        G[left + j] |= rock[j] << down


MIN_CYCLE_LEN = lcm([5, len(data)])

def p(epoch):
    height = 0
    prev_h = -1
    diff = []
    for i in range(0, epoch):
        down = height + 3
        if i > MIN_CYCLE_LEN and epoch % MIN_CYCLE_LEN == i % MIN_CYCLE_LEN:
            if prev_h>-1:
                diff.append(height-prev_h)
            prev_h = height
            if diff :
                print(diff)
                # lt, rt = seq[:len(seq) // 2], seq[len(seq) // 2:]
                # print(lt, rt)
                # if lt == rt:
                #     print('period', lt, 'len:', len(lt))
                #     remain = epoch - i
                #     cycle_len = len(lt)
                #     part_cycle_sum = sum(lt[:remain % cycle_len // 5])
                #     total = remain // cycle_len * sum(lt) + part_cycle_sum + prev
                #     print(total)
                #     break
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
        height = max(height, down + max(rock).bit_length())
    print(height)


p(2022)
# print_bin(G)
# print(max(G).bit_length())
# p(1000000000000)
