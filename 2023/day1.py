import re

from helper import *


def f(line):
    found = [int(x) for x in re.findall(r'\d', line)]
    return found[0] * 10 + found[-1]


def f2(line):
    def parse_int(letter: str):
        letters = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
        if letter.isdigit():
            return int(letter)
        if letter in letters:
            return letters.index(letter) + 1
        raise Exception(f"Bad format of letter:{letter}")

    m = re.findall(r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))', line)
    return parse_int(m[0]) * 10 + parse_int(m[-1])


p = Puzzle(2023, 1)
p.solve_line(f)
p.solve_line(f2)
