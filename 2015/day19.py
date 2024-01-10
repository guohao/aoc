from collections import defaultdict, deque
from functools import cache

from helper import *

data = """
H => HO
H => OH
O => HH

HOH
"""
data = raw_data(2015, 19)
raw_mapping, raw_input = data.strip().split('\n\n')
mappings = []
for line in raw_mapping.splitlines():
    s, t = list(map(str.strip, line.split(' => ')))
    mappings.append((s, t))


def p1():
    s = raw_input
    if len(s) == 0:
        return {''}
    ret = set()
    for k, v in mappings:
        for m in re.finditer(k, s):
            left = s[:m.start()]
            right = s[m.end():]
            ret.add(left + v + right)
    print(len(ret))


def p2():
    cells = sum([c.isupper() for c in raw_input])
    parentheses = raw_input.count('Rn') + raw_input.count('Ar')
    periods = 2 * raw_input.count('Y')
    print(cells - parentheses - periods - 1)

p1()
p2()