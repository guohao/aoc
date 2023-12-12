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


def grid_dict(all_lines: List[str]) -> dict:
    return {(i, j): all_lines[i][j] for i, j in
            itertools.product(range(len(all_lines)), range(len(all_lines[0])))}


def grid_find(grid: dict, find_str: str) -> List[tuple]:
    return [(i, j) for i, j in grid.keys() if grid[i, j] == find_str]


def grid_find_neighbors(grid: dict, find_str: str, i: int, j: int) -> List[tuple]:
    return [(i + x, j + y) for x, y in
            itertools.product(range(-1, 2), range(-1, 2)) if
            (i + x, j + y) in grid.keys() and grid[i + x, j + y] == find_str]


def extract_digit(line: str) -> List[int]:
    return [int(x) for x in line.split() if x.isdigit()]


def extract_num(line: str) -> List[int]:
    return [int(x) for x in re.findall(r'\d+', line)]


def grid_list(all_lines: List[str]) -> List[List[str]]:
    return [list(line) for line in all_lines]


def raw_data(year: int, day: int) -> str:
    elf.download_input_if_not_exist(year, day)
    file_name = elf.day_data_file_name(year, day)
    with open(file_name, 'r') as file:
        return file.read()
