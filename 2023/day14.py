import functools
from collections import defaultdict, deque

from helper import *


@functools.cache
def one_cycle(data: str) -> str:
    lines = grid_2d(data.strip())
    lines = rotate_matrix_90_anticlockwise(lines)
    move_grid(lines)
    # west
    lines = rotate_matrix_90_clockwise(lines)
    move_grid(lines)
    # south
    lines = rotate_matrix_90_clockwise(lines)
    move_grid(lines)
    # east
    lines = rotate_matrix_90_clockwise(lines)
    move_grid(lines)
    lines = rotate_matrix_90_clockwise(lines)
    lines = rotate_matrix_90_clockwise(lines)
    return '\n'.join("".join(line) for line in lines)


def move_grid(lines: List[List[str]]):
    def move_left(ll: List[str]):
        for i, c in enumerate(ll):
            if c != '.':
                continue
            for j in range(i + 1, len(ll)):
                if ll[j] == '#':
                    break
                if ll[j] == 'O':
                    ll[i] = 'O'
                    ll[j] = '.'
                    break

    for line in lines:
        move_left(line)


def count_score(ll: List[str]) -> int:
    cnt = 0
    for i in range(len(ll)):
        s = len(ll) - i
        if ll[i] == 'O':
            cnt += s
    return cnt


data = raw_data(2023, 14)
p1_in = rotate_matrix_90_anticlockwise(grid_2d(data))
move_grid(p1_in)
score = sum(count_score(line) for line in p1_in)

print(score)

for _ in range(1000000000):
    data = one_cycle(data)

score = sum(count_score(line) for line in rotate_matrix_90_anticlockwise(grid_2d(data)))
print(score)
