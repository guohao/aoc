import itertools
import math
import re
from typing import List

import elf


def lcm(a: int, b: int) -> int:
    return a * b // math.gcd(a, b)


def cmp(a, b):
    return (a > b) - (a < b)


def lines(data: str) -> List[str]:
    all_lines = data.strip().splitlines()
    return [line.strip() for line in all_lines if line and len(line.strip()) > 0]


def grid_2d(raw_data: str) -> List[List[str]]:
    return [list(row) for row in raw_data.strip().splitlines()]


def grid_dict(all_lines: List[str]) -> dict:
    return {(i, j): all_lines[i][j] for i, j in
            itertools.product(range(len(all_lines)), range(len(all_lines[0])))}


def grid_find_first(grid: dict, find_str: str) -> tuple:
    return grid_find(grid, find_str)[0]


def grid_find(grid: dict, find_str: str) -> List[tuple]:
    return [(i, j) for i, j in grid.keys() if grid[i, j] == find_str]


def grid_find_neighbors(grid: dict, p: tuple[int, int]) -> List[tuple]:
    i = p[0]
    j = p[1]
    return [(i + x, j + y) for x, y in
            itertools.product(range(-1, 2), range(-1, 2)) if
            (i + x, j + y) in grid.keys() and (x, y) != (0, 0)]


def grid_find_4_neighbors(grid: dict, p: tuple[int, int]) -> List[tuple]:
    i = p[0]
    j = p[1]
    return [(i + x, j + y) for x, y in
            [(0, 1), (1, 0), (0, -1), (-1, 0)] if
            (i + x, j + y) in grid.keys() and (x, y) != (0, 0)]


def extract_digit(line: str) -> List[int]:
    return [int(x) for x in line.split() if x.isdigit()]


def extract_num(line: str) -> tuple[int]:
    return tuple(int(x) for x in re.findall(r'\d+', line))


def grid_list(all_lines: List[str]) -> List[List[str]]:
    return [list(line) for line in all_lines]


def raw_data(year: int, day: int) -> str:
    elf.download_input_if_not_exist(year, day)
    file_name = elf.day_data_file_name(year, day)
    with open(file_name, 'r') as file:
        return file.read()


def patterns(data: str) -> List[List[str]]:
    return [x.splitlines() for x in data.strip().split('\n\n')]


def rotate_matrix_90_clockwise(matrix) -> List[List]:
    return [list(row) for row in zip(*matrix[::-1])]


def rotate_matrix_90_anticlockwise(matrix) -> List[List]:
    return [list(row) for row in zip(*matrix)][::-1]


def count_differences_in_lists(list1, list2):
    return sum(sum(ch1 != ch2 for ch1, ch2 in zip(str1, str2)) for str1, str2 in zip(list1, list2))


def count_intersect(a, b):
    return len(list(set(a) & set(b)))


def intersect(a, b):
    return list(set(a) & set(b))


def print_lines(lines):
    print()
    for line in lines:
        print(line)
    print()


class Puzzle:
    def __init__(self, year: int, day: int):
        self.year = 2023
        self.day = 1
        self.data = raw_data(year, day)

    def solve_raw(self, function):
        ret = function(self.data)
        print(ret)
        return ret

    def solve_lines(self, function):
        ret = function(lines(self.data))
        print(ret)
        return ret

    def solve_line(self, function):
        ret = sum(function(line) for line in lines(self.data))
        print(ret)
        return ret

    def solve_eline(self, function):
        ret = sum(function(i, line) for i, line in enumerate(lines(self.data)))
        print(ret)
        return ret

    def solve_pattern(self, function):
        ret = sum(function(pattern) for pattern in patterns(self.data))
        print(ret)
        return ret
