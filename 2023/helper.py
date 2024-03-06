import math
import re
from typing import List

import elf


def lcm(arr: List[int]) -> int:
    x = 1
    for c in arr:
        x = math.lcm(x, c)
    return x


def cmp(a, b):
    return (a > b) - (a < b)


def lines(data: str) -> List[str]:
    all_lines = data.strip().splitlines()
    return [line.strip() for line in all_lines if line and len(line.strip()) > 0]


def neighbors_2d(grid: dict[tuple[int, int], str], p: tuple[int, int]) -> List[tuple[int, int]]:
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        np = (p[0] + dx, p[1] + dy)
        if np in grid:
            yield np


def grid(data: str) -> dict[tuple[int, int], str]:
    all_lines = lines(data)
    return {(i, j): all_lines[i][j] for i in range(len(all_lines)) for j in range(len(all_lines[i]))}


def int_grid(data: str) -> dict[tuple[int, int], int]:
    all_lines = lines(data)
    return {(i, j): int(all_lines[i][j]) for i in range(len(all_lines)) for j in range(len(all_lines[i]))}


def digits(line: str) -> List[int]:
    return [int(x) for x in re.findall(r'\d', line)]


def nums(line: str) -> List[int]:
    return ints(line)


def ints(line: str) -> List[int]:
    return [int(x) for x in re.findall(r'[-+]?\d+', line)]




def patterns(data: str) -> List[List[str]]:
    return [x.splitlines() for x in data.strip().split('\n\n')]


def rotate_matrix_90_clockwise(matrix) -> List[List]:
    return [list(row) for row in zip(*matrix[::-1])]


def rotate_in_place(matrix: List[List], clockwise=True):
    if clockwise:
        r = rotate_matrix_90_clockwise(matrix)
    else:
        r = rotate_matrix_90_anticlockwise(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = r[i][j]


def rotate_matrix_90_anticlockwise(matrix) -> List[List]:
    return [list(row) for row in zip(*matrix)][::-1]


def print_lines(lines):
    print()
    for line in lines:
        print(line)
    print()
