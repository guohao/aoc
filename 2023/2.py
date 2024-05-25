import math
import re


def p1ss(line: str):
    constraints = {'red': 12, 'green': 13, 'blue': 14}
    gid = list(map(int, re.findall(r'Game (\d+)', line)))[0]
    for m in re.findall(r'(\d+) (blue|red|green)', line):
        if int(m[0]) > constraints[m[1]]:
            return 0
    return gid


def p2ss(line: str):
    max_count = {c: 0 for c in ['blue', 'red', 'green']}
    for m in re.findall(r'(\d+) (blue|red|green)', line):
        max_count[m[1]] = max(max_count[m[1]], int(m[0]))
    return math.prod(max_count.values())
