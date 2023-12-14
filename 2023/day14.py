import functools

from helper import *


@functools.cache
def move_cycle(data: str) -> str:
    lines = grid_2d(data.strip())
    move(lines)
    rotate_in_place(lines)
    move(lines)
    rotate_in_place(lines)
    move(lines)
    rotate_in_place(lines)
    move(lines)
    rotate_in_place(lines)
    return '\n'.join("".join(line) for line in lines)


def move(lines: List[List[str]]):
    for i, j in itertools.product(range(len(lines)), range(len(lines[0]))):
        if lines[i][j] != '.':
            continue
        for k in range(i + 1, len(lines)):
            if lines[k][j] == '#':
                break
            if lines[k][j] == 'O':
                lines[i][j] = 'O'
                lines[k][j] = '.'
                break


def score_of(lines: List[List[str]]) -> int:
    ret = 0
    for i in range(len(lines)):
        ss = len(lines) - i
        for j in range(len(lines[0])):
            if lines[i][j] == 'O':
                ret += ss
    return ret


data = raw_data(2023, 14)
g = grid_2d(data)
move(g)
print(score_of(g))

for _ in range(1000000000):
    data = move_cycle(data)

print(score_of(grid_2d(data)))
