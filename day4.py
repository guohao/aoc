import re
from typing import List

from day import Day


def count_winning(line: str) -> int:
    n = re.findall(r'\d+', line.split('|')[0].split(':')[1])
    m = re.findall(r'\d+', line.split('|')[1])
    return sum(x in n for x in m)


class Day4(Day):

    def __init__(self):
        super().__init__(day=4)

    def part_one(self, lines: List[str]) -> int:
        return sum([int(2 ** (count_winning(line) - 1)) for line in lines])

    def part_two(self, lines: List[str]) -> int:
        d = {x: 1 for x in range(len(lines))}
        for i in range(len(lines)):
            wining = count_winning(lines[i])
            for j in range(i + 1, wining + i + 1):
                d[j] = d[j] + d[i]
        return sum(d.values())


if __name__ == '__main__':
    Day4().run()
