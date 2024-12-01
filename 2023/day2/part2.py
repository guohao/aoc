import math
import re
import sys
from collections import defaultdict

lines = [line.strip() for line in sys.stdin.readlines()]
t = 0
for line in lines:
    cells = line.split(':')
    c_max = defaultdict(int)
    i = int(re.findall(r'-?\d+', cells[0])[0])
    for count, color in map(str.split, re.findall('|'.join(r'\d+ ' + x for x in ['red', 'blue', 'green']), cells[1])):
        c_max[color] = max(c_max[color], int(count))
    t += math.prod(c_max.values())

print(t)
