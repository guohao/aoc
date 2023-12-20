import re
from collections import defaultdict

from helper import *

data = raw_data(2023, 4)
lines = lines(data)
ans = 0
for line in lines:
    line = line.split(":")[1]
    a, b = [list(map(nums, part.split())) for part in line.split("|")]
    c = len([x for x in a if x in b])
    if c > 0:
        ans += 2 ** (c - 1)
print(ans)

d = defaultdict(lambda: 1)
d[0] = 1
for i, line in enumerate(lines, start=1):
    line = line.split(":")[1].strip()
    a, b = [list(map(nums, part.split())) for part in line.split("|")]
    c = len([x for x in a if x in b])
    for j in range(i + 1, i + 1 + c):
        d[j] += d[i]

print(sum(d.values()))
