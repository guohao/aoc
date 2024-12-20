import itertools
import math
import re
import sys

ins = []
for line in sys.stdin.readlines():
    line = line.strip()
    digits = list(map(int, re.findall(r'-?\d+', line)))
    ins.append(digits)

r = 0
for c in itertools.combinations_with_replacement(list(range(len(ins))), 100):
    s = [0] * 5
    for i in c:
        for j in range(len(s)):
            s[j] += ins[i][j]
    if any(x < 0 for x in s):
        continue
    if s[-1] != 500:
        continue
    r = max(math.prod(s[:-1]), r)
print(r)
