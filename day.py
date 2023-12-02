from typing import List

import io_utils


class Day:
    def __init__(self, day):
        self.day = day

    def part_one(self, lines: List[str]) -> int:
        pass

    def part_two(self, lines: List[str]) -> int:
        pass

    def run(self):
        lines = io_utils.get_day_input(self.day)
        ans1 = self.part_one(lines)
        print(f'ans1:{ans1}')
        ans2 = self.part_two(lines)
        print(f'ans2:{ans2}')
