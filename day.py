import logging
from typing import List

from common import io_utils

logging.basicConfig(level=logging.INFO)


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
        logging.info(f'Answer of part one is : {ans1}')
        ans2 = self.part_two(lines)
        logging.info(f'Answer of part two is : {ans2}')
