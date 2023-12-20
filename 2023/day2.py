from collections import defaultdict
from functools import reduce

from helper import *


def f(i, line):
    if not re.findall(r'((1[3-9]|[2-9]\d) red)|((1[5-9]|[2-9]\d) blue)|((1[4-9]|[2-9]\d) green)', line):
        return i + 1
    return 0


def f2(line):
    d = defaultdict(lambda: 0)
    for m in re.finditer(r'\d+\s+(blue|green|red)', line):
        count, color = m.group().split(' ')
        d[color] = max(int(count), d[color])
    return reduce(lambda a, b: a * b, d.values())


lines = lines(raw_data(2023, 2))
print(sum(f(i, line) for i, line in enumerate(lines)))
print(sum(f2(line) for line in lines))
