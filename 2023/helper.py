import itertools
import math
import re
from typing import List

import elf
import nographs


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


def grid_2d(maze: List[str]) -> nographs.Array:
    return nographs.Array(maze)


def nums(line: str) -> List[int]:
    return [int(x) for x in line.split() if x.isdigit()]


def raw_data(year: int, day: int) -> str:
    elf.download_input_if_not_exist(year, day)
    file_name = elf.day_data_file_name(year, day)
    with open(file_name, 'r') as file:
        return file.read()


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
