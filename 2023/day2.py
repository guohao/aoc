from collections import defaultdict
from functools import reduce

from helper import *


def extract_count(line: str):
    counts = []
    for reveal in line.split(':')[1].split(";"):
        for play in reveal.split(','):
            count, color = play.split()
            counts.append((int(count), color.strip()))
    return counts


def p1():
    ans = 0
    for i, line in enumerate(lines, start=1):
        match = True
        for count, color in extract_count(line):
            if color == 'red' and count > 12:
                match = False
                break
            elif color == 'green' and count > 13:
                match = False
                break
            elif color == 'blue' and count > 14:
                match = False
                break
        if match:
            ans += i
    print(ans)


def p2():
    ans = 0
    for i, line in enumerate(lines, start=1):
        fewest = defaultdict(lambda: 0)
        for count, color in extract_count(line):
            fewest[color] = max(count, fewest[color])
        ans += reduce(lambda a, b: a * b, fewest.values())
    print(ans)


lines = lines(raw_data(2023, 2))
p1()
p2()
