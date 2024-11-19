import itertools
import math
import re

ins = []
try:
    while True:
        ins.append(list(map(int, re.findall(r'-?\d+', input()))))
except EOFError:
    pass

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
