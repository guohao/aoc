from typing import List

from day import Day


def p1f(line: str) -> int:
    return 0


def p2f(line: str) -> int:
    return 0


class Day3(Day):

    def __init__(self):
        super().__init__(day=3)

    def part_one(self, lines: List[str]) -> int:
        ret = 0
        for i, line in enumerate(lines):
            ret += p1f(line)
        return ret

    def part_two(self, lines: List[str]) -> int:
        ret = 0
        for line in lines:
            ret += p2f(line)
        return ret


if __name__ == '__main__':
    Day3().run()
