import math
import re

import sys

data = sys.stdin.read().strip()

parts = data.split('\n\n')
holes = []
for line in parts[0].splitlines():
    ns = list(map(int, re.findall(r'\d+', line)))
    for i in range(0, len(ns), 2):
        holes.append((ns[i], ns[i + 1]))
ans = 0


def not_match(n) -> bool:
    for a, b in holes:
        if a <= n <= b:
            return False
    return True


for line in parts[2].splitlines()[1:]:
    for n in map(int, line.split(',')):
        if not_match(n):
            ans += n
print(ans)
