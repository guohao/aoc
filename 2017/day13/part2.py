import sys
import re
from itertools import count

lines = [line.strip() for line in sys.stdin.readlines()]
drs = []
for line in lines:
    drs.append(list(map(int, re.findall(r'-?\d+', line))))
for i in count():
    if all((i + d) % (2 * r - 2) for d, r in drs):
        print(i)
        break
