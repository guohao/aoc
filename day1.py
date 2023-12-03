import re
from typing import List

from day import Day


def parse_int(letter: str):
    if letter.isdigit():
        return int(letter)
    letters = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    if letter in letters:
        return letters.index(letter) + 1
    raise Exception(f"Bad format of letter:{letter}")


class Day1(Day):
    def __init__(self):
        super().__init__(day=1)

    def part_one(self, lines: List[str]) -> int:
        result = 0
        for line in lines:
            found = [int(x) for x in re.findall(r'\d', line)]
            result += found[0] * 10 + found[-1]
        return result

    def part_two(self, lines: List[str]):
        result = 0
        for line in lines:
            m = re.findall(r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))', line)
            result += parse_int(m[0]) * 10 + parse_int(m[-1])
        return result


if __name__ == '__main__':
    Day1().run()
