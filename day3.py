import re as regex
from typing import List

from day import Day


class Day3(Day):

    def __init__(self):
        super().__init__(day=3)

    def part_one(self, lines: List[str]) -> int:
        ret = 0
        for i, line in enumerate(lines):
            for m in regex.finditer(r'\d+', line):
                x = [x for x in range(i - 1, i + 2)]
                y = [y for y in range(m.start() - 1, m.end() + 1)]
                idx = [(a, b) for a in x for b in y]
                count = sum(0 <= a < len(lines) and 0 <= b < len(line) and lines[a][b] != '.'
                            and not (a == i and m.start() <= b < m.end())
                            for a, b in idx)
                if count > 0:
                    ret += int(m.group())
        return ret

    def part_two(self, lines: List[str]) -> int:
        d = {}
        for i, line in enumerate(lines):
            for m in regex.finditer(r'\d+', line):
                x = [x for x in range(i - 1, i + 2)]
                y = [y for y in range(m.start() - 1, m.end() + 1)]
                idx = [(a, b) for a in x for b in y]
                stars = [(a, b) for a, b in idx if
                         0 <= a < len(lines) and 0 <= b < len(line) and lines[a][b] == '*' and not (
                                 a == i and m.start() <= b < m.end())]
                for s in stars:
                    d.setdefault(s, []).append(int(m.group()))

        return sum(v[0] * v[1] for v in d.values() if len(v) == 2)


if __name__ == '__main__':
    Day3().run()
