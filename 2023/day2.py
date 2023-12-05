import re
from collections import defaultdict
from functools import reduce
from typing import List

from common import io_utils


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


data = io_utils.get_data(2023, 2)
lines = io_utils.raw_str_to_lines(data)
ans1 = 0
ans2 = 0
for i, line in enumerate(lines):
    if not re.findall(r'((1[3-9]|[2-9]\d) red)|((1[5-9]|[2-9]\d) blue)|((1[4-9]|[2-9]\d) green)', line):
        ans1 += i + 1
    d = defaultdict(lambda: 0)
    for m in re.finditer(r'\d+\s+(blue|green|red)', line):
        count, color = m.group().split(' ')
        d[color] = max(int(count), d[color])
    ans2 += reduce(lambda a, b: a * b, d.values())
print(ans1)
print(ans2)
