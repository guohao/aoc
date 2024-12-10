import re
import sys

lines = [l.strip() for l in sys.stdin.readlines()]

cubes = [list(map(int, re.findall(r'-?\d+', line))) for line in lines]
ans = 6 * len(cubes)
for i, a in enumerate(cubes):
    for b in cubes[:i]:
        if sum(abs(a[k] - b[k]) for k in range(3)) == 1:
            ans -= 2
print(ans)
