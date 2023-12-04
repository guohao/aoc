import re
from typing import List

from common import io_utils


def parse_int(letter: str):
    letters = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    if letter.isdigit():
        return int(letter)
    if letter in letters:
        return letters.index(letter) + 1
    raise Exception(f"Bad format of letter:{letter}")


def pl(lines: List[str]):
    ans1 = 0
    ans2 = 0
    for line in lines:
        found = [int(x) for x in re.findall(r'\d', line)]
        m = re.findall(r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))', line)
        ans1 += found[0] * 10 + found[-1]
        ans2 += parse_int(m[0]) * 10 + parse_int(m[-1])
    print(ans1)
    print(ans2)


if __name__ == '__main__':
    data = io_utils.get_data(2023, 1)
    data = io_utils.raw_str_to_lines(data)
    pl(data)
