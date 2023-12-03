import re
from functools import reduce
from typing import List

from day import Day


def extract_game(line: str) -> List[List[int]]:
    game = []
    for play in line.split(':')[1].split(';'):
        once_list = [0, 0, 0]
        for once in play.strip().split(','):
            once = once.strip()
            num = int(once.split(' ')[0].strip())
            color = once.split(' ')[1].strip()
            if color == 'blue':
                once_list[0] = num
            elif color == 'red':
                once_list[1] = num
            elif color == 'green':
                once_list[2] = num
            else:
                raise Exception(f"bad input:{once}")
            game.append(once_list)
    return game


class Day2(Day):

    def __init__(self):
        super().__init__(day=2)

    def part_one(self, lines: List[str]) -> int:
        """
        12 red cubes, 13 green cubes, and 14 blue cubes
        Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
        :param line:
        """
        ret = 0
        for i, line in enumerate(lines):
            if not re.findall(r'((1[3-9]|[2-9]\d) red)|((1[5-9]|[2-9]\d) blue)|((1[4-9]|[2-9]\d) green)', line):
                ret += i + 1
        return ret

    def part_two(self, lines: List[str]) -> int:
        ret = 0
        for line in lines:
            d = {}
            for m in re.finditer(r'\d+\s+(blue|green|red)', line):
                count, color = m.group().split(' ')
                d.setdefault(color, 0)
                d[color] = max(int(count), d[color])
            ret += reduce(lambda a, b: a * b, d.values())
        return ret


if __name__ == '__main__':
    Day2().run()
